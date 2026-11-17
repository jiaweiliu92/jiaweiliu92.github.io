import json
import os
import tempfile
import time
from datetime import datetime, timezone

from scholarly import scholarly, ProxyGenerator


# -----------------------------
# Configuration
# -----------------------------

MAX_ATTEMPTS = 3
WAIT_SECONDS = 60

# ScraperAPI may retry internally for up to approximately 60 seconds.
SCHOLARLY_TIMEOUT = 70
SCHOLARLY_RETRIES = 1

FREE_PROXY_TIMEOUT = 1
FREE_PROXY_WAIT_TIME = 20

RESULTS_DIR = "results"
PUBLICATION_SECTIONS = ["basics", "indices", "counts", "publications"]


# -----------------------------
# Connection helpers
# -----------------------------

def install_connection(proxy_generator):
    """Use the selected connection for both scholarly request paths.

    scholarly 1.7.11 has primary and secondary proxy generators. Some
    citation requests use the secondary generator. Passing the same
    configured generator twice prevents an unintended FreeProxies fallback.
    """
    scholarly.use_proxy(proxy_generator, proxy_generator)


def fetch_and_fill_author(scholar_id, connection_name):
    print(f"[{connection_name}] Fetching author profile...", flush=True)
    author = scholarly.search_author_id(scholar_id)

    print(
        f"[{connection_name}] Fetching publication and citation details...",
        flush=True,
    )
    scholarly.fill(author, sections=PUBLICATION_SECTIONS)
    return author


def try_scraperapi(scholar_id, api_key):
    print("Trying ScraperAPI...", flush=True)
    proxy_generator = ProxyGenerator()

    # scholarly's ScraperAPI helper checks account access and proxy connectivity.
    # Never print or log api_key.
    proxy_ready = proxy_generator.ScraperAPI(api_key)
    if not proxy_ready:
        raise RuntimeError(
            "ScraperAPI initialization returned False. Check the API key, "
            "account status, usage limit, and proxy access in ScraperAPI."
        )

    install_connection(proxy_generator)
    print("ScraperAPI configured for both scholarly request paths.", flush=True)
    return fetch_and_fill_author(scholar_id, "ScraperAPI")


def try_direct(scholar_id):
    print("Trying direct Google Scholar connection...", flush=True)

    # Do not pass a null generator to use_proxy: in scholarly 1.7.11, that does not
    # reset the existing primary proxy. A fresh, unconfigured generator creates
    # direct HTTP sessions; assign it to both request paths explicitly.
    direct_generator = ProxyGenerator()
    install_connection(direct_generator)

    return fetch_and_fill_author(scholar_id, "Direct")


def try_freeproxies(scholar_id):
    print("Trying scholarly FreeProxies fallback...", flush=True)
    proxy_generator = ProxyGenerator()

    proxy_ready = proxy_generator.FreeProxies(
        timeout=FREE_PROXY_TIMEOUT,
        wait_time=FREE_PROXY_WAIT_TIME,
    )
    if not proxy_ready:
        raise RuntimeError("FreeProxies initialization returned False.")

    install_connection(proxy_generator)
    print("FreeProxies configured for both scholarly request paths.", flush=True)
    return fetch_and_fill_author(scholar_id, "FreeProxies")


# -----------------------------
# Fetch Google Scholar data
# -----------------------------

def fetch_author_data():
    scholar_id = os.environ.get("GOOGLE_SCHOLAR_ID")
    if not scholar_id:
        raise ValueError("GOOGLE_SCHOLAR_ID is not configured.")

    scraperapi_key = os.environ.get("SCRAPERAPI_API_KEY")

    scholarly.set_timeout(SCHOLARLY_TIMEOUT)
    scholarly.set_retries(SCHOLARLY_RETRIES)

    if scraperapi_key:
        print("SCRAPERAPI_API_KEY is present.", flush=True)
    else:
        print("SCRAPERAPI_API_KEY is missing; ScraperAPI will be skipped.", flush=True)

    for attempt in range(1, MAX_ATTEMPTS + 1):
        print(f"========== Attempt {attempt}/{MAX_ATTEMPTS} ==========", flush=True)

        # 1. ScraperAPI
        if scraperapi_key:
            try:
                return try_scraperapi(scholar_id, scraperapi_key)
            except Exception as error:
                print(
                    "ScraperAPI stage failed: "
                    f"{type(error).__name__}: {error}",
                    flush=True,
                )

        # 2. Direct Google Scholar
        try:
            return try_direct(scholar_id)
        except Exception as error:
            print(
                "Direct connection stage failed: "
                f"{type(error).__name__}: {error}",
                flush=True,
            )

        # 3. scholarly FreeProxies
        try:
            return try_freeproxies(scholar_id)
        except Exception as error:
            print(
                "FreeProxies stage failed: "
                f"{type(error).__name__}: {error}",
                flush=True,
            )

        if attempt < MAX_ATTEMPTS:
            print(
                f"All connection methods failed. Waiting {WAIT_SECONDS} "
                "seconds before retrying the sequence.",
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

    # An empty list can be valid; a non-empty list without usable IDs is suspicious.
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

    print("========== Update completed ==========" , flush=True)
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
