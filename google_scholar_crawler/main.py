import json
import os
import tempfile
import time
from datetime import datetime, timezone

from scholarly import scholarly, ProxyGenerator


# -----------------------------
# Configuration
# -----------------------------

MAX_ATTEMPTS = 2
WAIT_SECONDS = 60

# ScraperAPI can retry internally for up to about 60 seconds. Keep the
# scholarly timeout longer so it does not cut that process short.
SCHOLARLY_TIMEOUT = 70
SCHOLARLY_RETRIES = 1

FREE_PROXY_TIMEOUT = 1
FREE_PROXY_WAIT_TIME = 20

RESULTS_DIR = "results"
PUBLICATION_SECTIONS = ["basics", "indices", "counts", "publications"]


# -----------------------------
# Fetch Google Scholar data
# -----------------------------

def fetch_and_fill_author(scholar_id):
    """Fetch an author profile and its publication details."""
    author = scholarly.search_author_id(scholar_id)
    scholarly.fill(author, sections=PUBLICATION_SECTIONS)
    return author


def fetch_author_data():
    scholar_id = os.environ.get("GOOGLE_SCHOLAR_ID")
    if not scholar_id:
        raise ValueError("GOOGLE_SCHOLAR_ID is not configured.")

    scraperapi_key = os.environ.get("SCRAPERAPI_API_KEY")

    scholarly.set_timeout(SCHOLARLY_TIMEOUT)
    scholarly.set_retries(SCHOLARLY_RETRIES)

    if scraperapi_key:
        print("SCRAPERAPI_API_KEY is configured.", flush=True)
    else:
        print(
            "SCRAPERAPI_API_KEY is not configured; ScraperAPI will be skipped.",
            flush=True,
        )

    for attempt in range(1, MAX_ATTEMPTS + 1):
        print(f"========== Attempt {attempt}/{MAX_ATTEMPTS} ==========", flush=True)

        # 1. ScraperAPI (only when its GitHub Secret is configured).
        if scraperapi_key:
            try:
                print("Trying ScraperAPI...", flush=True)
                proxy_generator = ProxyGenerator()
                proxy_ready = proxy_generator.ScraperAPI(scraperapi_key)
                if not proxy_ready:
                    raise RuntimeError("ScraperAPI proxy setup returned False.")

                scholarly.use_proxy(proxy_generator)
                author = fetch_and_fill_author(scholar_id)
                print("ScraperAPI connection succeeded.", flush=True)
                return author
            except Exception as scraperapi_error:
                print(
                    "ScraperAPI failed: "
                    f"{type(scraperapi_error).__name__}: {scraperapi_error}",
                    flush=True,
                )

        # 2. Direct connection. Explicitly clear any previously configured proxy.
        try:
            print("Trying direct Google Scholar connection...", flush=True)
            scholarly.use_proxy(None)
            author = fetch_and_fill_author(scholar_id)
            print("Direct connection succeeded.", flush=True)
            return author
        except Exception as direct_error:
            print(
                "Direct connection failed: "
                f"{type(direct_error).__name__}: {direct_error}",
                flush=True,
            )

        # 3. scholarly's free proxy pool.
        try:
            print("Trying scholarly FreeProxies fallback...", flush=True)
            proxy_generator = ProxyGenerator()
            proxy_ready = proxy_generator.FreeProxies(
                timeout=FREE_PROXY_TIMEOUT,
                wait_time=FREE_PROXY_WAIT_TIME,
            )
            if not proxy_ready:
                raise RuntimeError("FreeProxies setup returned False.")

            scholarly.use_proxy(proxy_generator)
            author = fetch_and_fill_author(scholar_id)
            print("FreeProxies connection succeeded.", flush=True)
            return author
        except Exception as proxy_error:
            print(
                "FreeProxies failed: "
                f"{type(proxy_error).__name__}: {proxy_error}",
                flush=True,
            )

        if attempt < MAX_ATTEMPTS:
            print(
                f"All connection methods failed. Waiting {WAIT_SECONDS} seconds "
                "before retry.",
                flush=True,
            )
            time.sleep(WAIT_SECONDS)

    raise RuntimeError(
        "Unable to retrieve Google Scholar data using ScraperAPI, direct "
        "connection, or scholarly FreeProxies after all attempts."
    )


# -----------------------------
# Validate and prepare data
# -----------------------------

def prepare_author_data(author):
    if not isinstance(author, dict):
        raise ValueError("Google Scholar returned invalid author data.")

    if not author.get("name"):
        raise ValueError("Author name is missing.")

    if "citedby" not in author or author["citedby"] is None:
        raise ValueError("Citation count is missing.")

    try:
        citedby = int(author["citedby"])
    except (TypeError, ValueError) as error:
        raise ValueError("Citation count is not a valid integer.") from error

    if citedby < 0:
        raise ValueError("Citation count cannot be negative.")

    raw_publications = author.get("publications")
    if not isinstance(raw_publications, list):
        raise ValueError("Publications data is missing or is not a list.")

    publications = {}
    for publication in raw_publications:
        if not isinstance(publication, dict):
            continue
        publication_id = publication.get("author_pub_id")
        if publication_id:
            publications[publication_id] = publication

    # A truly empty list is allowed; a non-empty list without usable IDs is not.
    if raw_publications and not publications:
        raise ValueError(
            "Publication records were returned, but none had author_pub_id."
        )

    author_data = author.copy()
    author_data["citedby"] = citedby
    author_data["updated"] = datetime.now(timezone.utc).isoformat()
    author_data["publications"] = dict(sorted(publications.items()))
    return author_data


# -----------------------------
# Safe JSON writing
# -----------------------------

def write_json_temp(data, filepath):
    directory = os.path.dirname(filepath) or "."
    os.makedirs(directory, exist_ok=True)

    with tempfile.NamedTemporaryFile(
        mode="w",
        encoding="utf-8",
        dir=directory,
        suffix=".tmp",
        delete=False,
    ) as file:
        json.dump(data, file, ensure_ascii=False, indent=2)
        file.write("\n")
        file.flush()
        os.fsync(file.fileno())
        return file.name


def save_author_data(author):
    author_data = prepare_author_data(author)
    shieldio_data = {
        "schemaVersion": 1,
        "label": "citations",
        "message": str(author_data["citedby"]),
    }

    os.makedirs(RESULTS_DIR, exist_ok=True)
    author_path = os.path.join(RESULTS_DIR, "gs_data.json")
    shield_path = os.path.join(RESULTS_DIR, "gs_data_shieldsio.json")
    temporary_files = []

    try:
        # Serialize both outputs before replacing either destination.
        author_temp = write_json_temp(author_data, author_path)
        temporary_files.append(author_temp)
        shield_temp = write_json_temp(shieldio_data, shield_path)
        temporary_files.append(shield_temp)

        os.replace(author_temp, author_path)
        temporary_files.remove(author_temp)
        os.replace(shield_temp, shield_path)
        temporary_files.remove(shield_temp)
    finally:
        for temporary_file in temporary_files:
            if os.path.exists(temporary_file):
                os.remove(temporary_file)

    print("========== Update completed ==========", flush=True)
    print(f"Author: {author_data['name']}", flush=True)
    print(f"Citations: {author_data['citedby']}", flush=True)
    print(f"Publications: {len(author_data['publications'])}", flush=True)
    print(f"Updated: {author_data['updated']}", flush=True)


# -----------------------------
# Main
# -----------------------------

def main():
    author = fetch_author_data()
    save_author_data(author)


if __name__ == "__main__":
    main()
