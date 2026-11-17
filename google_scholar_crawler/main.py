"""Fetch the full Google Scholar author profile and citation statistics.

Preserves the original crawler's data collection and JSON output:
- author basics, indices, yearly citation counts, and all publications;
- publication entries keyed by author_pub_id;
- gs_data.json and gs_data_shieldsio.json in the results directory.

Reliability changes are limited to bounded free-proxy discovery, explicit
primary/secondary proxy configuration, request timeouts, and finite retries.
"""

from scholarly import scholarly, ProxyGenerator
import json
import os
import signal
import sys
import time
from datetime import datetime

MAX_ATTEMPTS = 5
WAIT_SECONDS = 60

FREE_PROXY_TIMEOUT = 1
FREE_PROXY_WAIT_TIME = 30
FREE_PROXY_SETUP_TIMEOUT = 45

SCHOLARLY_TIMEOUT = 20
SCHOLARLY_RETRIES = 2


def configure_scholarly():
    """Configure finite request-level timeout and retry limits."""
    scholarly.set_timeout(SCHOLARLY_TIMEOUT)
    scholarly.set_retries(SCHOLARLY_RETRIES)


def _set_direct_access():
    """Use fresh, unconfigured sessions for both routes (no proxy lookup)."""
    direct_generator = ProxyGenerator()
    # Pass both slots explicitly. scholarly.use_proxy(pg) alone creates a
    # second FreeProxies generator internally when the secondary is omitted.
    scholarly.use_proxy(direct_generator, direct_generator)


def configure_free_proxy(attempt):
    """Try the original free rotating proxy method with a hard time bound."""
    proxy_generator = ProxyGenerator()

    print(
        "Attempt {}: searching for a working free proxy (max {} seconds).".format(
            attempt, FREE_PROXY_SETUP_TIMEOUT
        ),
        flush=True,
    )

    def proxy_setup_timeout(_signum, _frame):
        raise TimeoutError(
            "Free-proxy setup exceeded {} seconds.".format(
                FREE_PROXY_SETUP_TIMEOUT
            )
        )

    previous_handler = signal.signal(signal.SIGALRM, proxy_setup_timeout)
    try:
        signal.setitimer(signal.ITIMER_REAL, FREE_PROXY_SETUP_TIMEOUT)
        proxy_ready = proxy_generator.FreeProxies(
            timeout=FREE_PROXY_TIMEOUT,
            wait_time=FREE_PROXY_WAIT_TIME,
        )
    except Exception as exc:
        print(
            "Free-proxy setup failed: {}: {}".format(type(exc).__name__, exc),
            file=sys.stderr,
            flush=True,
        )
        proxy_ready = False
    finally:
        signal.setitimer(signal.ITIMER_REAL, 0)
        signal.signal(signal.SIGALRM, previous_handler)

    if proxy_ready:
        # Important: explicitly pass the same generator as primary and
        # secondary, preventing scholarly from silently creating another
        # default FreeProxies instance with its own unbounded setup loop.
        scholarly.use_proxy(proxy_generator, proxy_generator)
        print("Free rotating proxy configured for both request routes.", flush=True)
        return True

    print("No working free proxy was configured; switching to direct access.", flush=True)
    _set_direct_access()
    return False


def fetch_full_author():
    """Fetch the complete author profile, including all publications."""
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

    # Preserve the original data transformation used by the homepage.
    author["publications"] = {
        publication["author_pub_id"]: publication
        for publication in author["publications"]
    }
    author["updated"] = str(datetime.now())
    return author


def retrieve_author():
    """Retry the full crawl; fall back from proxy to direct access per attempt."""
    last_error = None

    for attempt in range(1, MAX_ATTEMPTS + 1):
        print("\nAttempt {}/{}:".format(attempt, MAX_ATTEMPTS), flush=True)
        proxy_ready = configure_free_proxy(attempt)

        try:
            author = fetch_full_author()
            access_mode = "free proxy" if proxy_ready else "direct"
            print("Attempt {} succeeded using {} access.".format(attempt, access_mode), flush=True)
            return author
        except Exception as request_error:
            last_error = request_error
            print(
                "Attempt {} failed: {}: {}".format(
                    attempt, type(request_error).__name__, request_error
                ),
                file=sys.stderr,
                flush=True,
            )

        # A proxy may pass its connectivity test but still be blocked by
        # Google Scholar. Retry this attempt once using explicitly direct
        # sessions; this does not invoke FreeProxies again.
        if proxy_ready:
            try:
                print("Retrying this attempt using direct access.", flush=True)
                _set_direct_access()
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
            print("Waiting {} seconds before the next attempt.".format(WAIT_SECONDS), flush=True)
            time.sleep(WAIT_SECONDS)

    raise RuntimeError(
        "All {} attempts to retrieve the full Google Scholar profile failed.".format(
            MAX_ATTEMPTS
        )
    ) from last_error


def main():
    configure_scholarly()
    author = retrieve_author()

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
    with open("results/gs_data_shieldsio.json", "w", encoding="utf-8") as outfile:
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
