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

# FreeProxies parameters:
# timeout: timeout for checking one proxy
# wait_time: maximum wait for a newer proxy list
PROXY_TIMEOUT = 1
PROXY_WAIT_TIME = 20

RESULTS_DIR = "results"
PUBLICATION_SECTIONS = ["basics", "indices", "counts", "publications"]


# -----------------------------
# Fetch Google Scholar data
# -----------------------------

def fetch_author_data():
    scholar_id = os.environ.get("GOOGLE_SCHOLAR_ID")
    if not scholar_id:
        raise ValueError("GOOGLE_SCHOLAR_ID is not configured.")

    # Keep the library's own retry behavior small and predictable.
    scholarly.set_timeout(20)
    scholarly.set_retries(1)

    for attempt in range(1, MAX_ATTEMPTS + 1):
        print(
            f"========== Attempt {attempt}/{MAX_ATTEMPTS} ==========",
            flush=True,
        )

        # Attempt 1: direct connection.
        try:
            print("Trying direct Google Scholar connection...", flush=True)
            scholarly.use_proxy(None)

            author = scholarly.search_author_id(scholar_id)
            scholarly.fill(author, sections=PUBLICATION_SECTIONS)

            print("Direct connection succeeded.", flush=True)
            return author

        except Exception as direct_error:
            print(
                f"Direct connection failed: {type(direct_error).__name__}: "
                f"{direct_error}",
                flush=True,
            )

        # Attempt 2: free proxy fallback.
        try:
            print("Trying free proxy fallback...", flush=True)
            proxy_generator = ProxyGenerator()

            proxy_ready = proxy_generator.FreeProxies(
                timeout=PROXY_TIMEOUT,
                wait_time=PROXY_WAIT_TIME,
            )
            if not proxy_ready:
                raise RuntimeError("Free proxy setup returned False.")

            scholarly.use_proxy(proxy_generator)

            author = scholarly.search_author_id(scholar_id)
            scholarly.fill(author, sections=PUBLICATION_SECTIONS)

            print("Free proxy connection succeeded.", flush=True)
            return author

        except Exception as proxy_error:
            print(
                f"Free proxy attempt failed: {type(proxy_error).__name__}: "
                f"{proxy_error}",
                flush=True,
            )

        if attempt < MAX_ATTEMPTS:
            print(
                f"Both connection methods failed. "
                f"Waiting {WAIT_SECONDS} seconds before retry.",
                flush=True,
            )
            time.sleep(WAIT_SECONDS)

    raise RuntimeError(
        "Unable to retrieve Google Scholar data using direct connection "
        "or free proxy after all attempts."
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

    # Do not reject a genuinely empty publication list. But if Scholar
    # returned records and none has an ID, treat that as suspicious.
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
        # Serialize both outputs successfully before replacing either file.
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
    print(
        f"Publications: {len(author_data['publications'])}",
        flush=True,
    )
    print(f"Updated: {author_data['updated']}", flush=True)


# -----------------------------
# Main
# -----------------------------

def main():
    author = fetch_author_data()
    save_author_data(author)


if __name__ == "__main__":
    main()
