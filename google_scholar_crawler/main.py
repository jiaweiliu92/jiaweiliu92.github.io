"""Fetch the full Google Scholar author profile and citation statistics.

This keeps the original homepage crawler's data collection and output format:
- author basics, indices, yearly citation counts, and all publications;
- publication entries keyed by author_pub_id;
- gs_data.json and gs_data_shieldsio.json in the results directory.

The changes are limited to bounded proxy discovery, request timeouts, and a
reasonable outer retry policy so a failed free-proxy lookup cannot occupy a
GitHub Actions runner for hours.
"""

from scholarly import scholarly, ProxyGenerator
import json
import os
import signal
import sys
import time
from datetime import datetime

# Keep retries, but avoid the original 100 attempts with a 10-minute pause.
MAX_ATTEMPTS = 5
WAIT_SECONDS = 60

# Keep using free rotating proxies. Bound the time spent discovering/testing
# them; FreeProxies' wait_time is the maximum discovery window.
FREE_PROXY_TIMEOUT = 1
FREE_PROXY_WAIT_TIME = 30
FREE_PROXY_SETUP_TIMEOUT = 45

# Bound requests made by scholarly itself. The full publication list is still
# fetched, so a run may take longer than a total-citations-only lookup.
SCHOLARLY_TIMEOUT = 20
SCHOLARLY_RETRIES = 2


def configure_scholarly():
    """Set finite per-request timeout and internal retry settings."""
    scholarly.set_timeout(SCHOLARLY_TIMEOUT)
    scholarly.set_retries(SCHOLARLY_RETRIES)


def configure_free_proxy(attempt):
    """Try the original free rotating proxy mechanism with bounded discovery."""
    # Clear any proxy configuration left by a previous attempt first.
    scholarly.use_proxy(None)

    proxy_generator = ProxyGenerator()
    try:
        print(
            "Attempt {}: searching for a working free proxy (max {} seconds).".format(
                attempt, FREE_PROXY_WAIT_TIME
            ),
            flush=True,
        )
        # scholarly 1.7.11 has an internal proxy retry loop. Its public
        # wait_time does not strictly bound every path through that loop, so
        # enforce a hard wall-clock limit around setup on the Ubuntu runner.
        def proxy_setup_timeout(_signum, _frame):
            raise TimeoutError(
                "Free-proxy setup exceeded {} seconds.".format(
                    FREE_PROXY_SETUP_TIMEOUT
                )
            )

        previous_handler = signal.signal(signal.SIGALRM, proxy_setup_timeout)
        signal.setitimer(signal.ITIMER_REAL, FREE_PROXY_SETUP_TIMEOUT)
        try:
            proxy_ready = proxy_generator.FreeProxies(
                timeout=FREE_PROXY_TIMEOUT,
                wait_time=FREE_PROXY_WAIT_TIME,
            )
        finally:
            signal.setitimer(signal.ITIMER_REAL, 0)
            signal.signal(signal.SIGALRM, previous_handler)
        if proxy_ready:
            scholarly.use_proxy(proxy_generator)
            print("Free rotating proxy configured.", flush=True)
            return True

        print("No working free proxy was found; will try direct access.", flush=True)
    except Exception as exc:
        print(
            "Free-proxy setup failed; will try direct access: {}: {}".format(
                type(exc).__name__, exc
            ),
            file=sys.stderr,
            flush=True,
        )

    scholarly.use_proxy(None)
    return False


def fetch_full_author():
    """Fetch the same full author sections as the original implementation."""
    scholar_id = os.environ.get("GOOGLE_SCHOLAR_ID", "").strip()
    if not scholar_id:
        raise RuntimeError(
            "GOOGLE_SCHOLAR_ID is empty. Check the repository Actions secret."
        )

    author = scholarly.search_author_id(scholar_id)
    author = scholarly.fill(
        author,
        sections=["basics", "indices", "counts", "publications"],
    )

    if not isinstance(author, dict):
        raise RuntimeError("Google Scholar returned an invalid author profile.")
    if "name" not in author or "citedby" not in author:
        raise RuntimeError("Google Scholar profile is missing name or citedby.")
    if "publications" not in author:
        raise RuntimeError("Google Scholar profile did not include publications.")

    # Preserve the original data transformation used by the website's
    # per-paper citation placeholders.
    author["publications"] = {
        publication["author_pub_id"]: publication
        for publication in author["publications"]
    }
    author["updated"] = str(datetime.now())
    return author


def retrieve_author():
    """Retry the full crawl; try direct access if a configured proxy fails."""
    last_error = None

    for attempt in range(1, MAX_ATTEMPTS + 1):
        print("\nAttempt {}/{}:".format(attempt, MAX_ATTEMPTS), flush=True)
        proxy_ready = configure_free_proxy(attempt)

        try:
            author = fetch_full_author()
            print("Attempt {} succeeded using {} access.".format(
                attempt, "proxy" if proxy_ready else "direct"
            ), flush=True)
            return author
        except Exception as proxy_error:
            last_error = proxy_error
            print(
                "Attempt {} failed: {}: {}".format(
                    attempt, type(proxy_error).__name__, proxy_error
                ),
                file=sys.stderr,
                flush=True,
            )

        # If a free proxy was configured but Scholar requests still failed,
        # make one direct-access fallback before waiting for the next attempt.
        if proxy_ready:
            try:
                print("Retrying this attempt without a proxy.", flush=True)
                scholarly.use_proxy(None)
                author = fetch_full_author()
                print("Direct-access fallback succeeded.", flush=True)
                return author
            except Exception as direct_error:
                last_error = direct_error
                print(
                    "Direct-access fallback failed: {}: {}".format(
                        type(direct_error).__name__, direct_error
                    ),
                    file=sys.stderr,
                    flush=True,
                )

        if attempt < MAX_ATTEMPTS:
            print("Waiting {} seconds before the next attempt.".format(
                WAIT_SECONDS
            ), flush=True)
            time.sleep(WAIT_SECONDS)

    raise RuntimeError(
        "All {} attempts to retrieve the full Google Scholar profile failed.".format(
            MAX_ATTEMPTS
        )
    ) from last_error


def main():
    configure_scholarly()
    author = retrieve_author()

    # Keep the original output paths and JSON schemas unchanged.
    name = author["name"]
    print("Retrieved profile for: {}".format(name), flush=True)
    print(json.dumps(author, indent=2, ensure_ascii=False))

    os.makedirs("results", exist_ok=True)
    with open("results/gs_data.json", "w", encoding="utf-8") as outfile:
        json.dump(author, outfile, ensure_ascii=False)

    shieldio_data = {
        "schemaVersion": 1,
        "label": "citations",
        "message": str(author["citedby"]),
    }
    with open(
        "results/gs_data_shieldsio.json", "w", encoding="utf-8"
    ) as outfile:
        json.dump(shieldio_data, outfile, ensure_ascii=False)

    print(
        "Saved full author profile and citation badge data. Publications: {}".format(
            len(author["publications"])
        ),
        flush=True,
    )


if __name__ == "__main__":
    try:
        main()
    except Exception as exc:
        print(
            "Crawler failed: {}: {}".format(type(exc).__name__, exc),
            file=sys.stderr,
            flush=True,
        )
        raise SystemExit(1)
