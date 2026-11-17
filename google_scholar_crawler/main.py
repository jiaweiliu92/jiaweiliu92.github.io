"""Fetch the full Google Scholar author profile and citation statistics.

The crawler keeps the original data collection and JSON output. Network access
uses the following fallback order on each attempt:
    1. ScraperAPI (when SCRAPERAPI_KEY is configured)
    2. scholarly's built-in FreeProxies provider
    3. direct access

All three routes are configured explicitly for both scholarly request paths so
that scholarly does not silently create another free-proxy generator.
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

# Free-proxy discovery limits.
FREE_PROXY_TIMEOUT = 1
FREE_PROXY_WAIT_TIME = 30
FREE_PROXY_SETUP_TIMEOUT = 45

# ScraperAPI's own proxy mode recommends allowing up to 60 seconds per request
# so that its internal proxy rotation/retries can finish.
SCRAPERAPI_SETUP_TIMEOUT = 20
SCRAPERAPI_REQUEST_TIMEOUT = 60

# Shorter timeout for the free-proxy and direct-access routes.
SCHOLARLY_TIMEOUT = 20
SCHOLARLY_RETRIES = 2


def configure_scholarly():
    """Set the normal timeout and retry limits used by the crawler."""
    scholarly.set_timeout(SCHOLARLY_TIMEOUT)
    scholarly.set_retries(SCHOLARLY_RETRIES)


def _run_with_alarm(timeout_seconds, operation, description):
    """Run a blocking proxy initialization step with a hard time limit.

    GitHub Actions runs this workflow on Linux, where SIGALRM is available.
    The previous signal handler/timer is restored after the operation.
    """
    if not hasattr(signal, "SIGALRM"):
        return operation()

    def timeout_handler(_signum, _frame):
        raise TimeoutError(
            "{} exceeded {} seconds.".format(description, timeout_seconds)
        )

    previous_handler = signal.getsignal(signal.SIGALRM)
    previous_timer = signal.getitimer(signal.ITIMER_REAL)
    signal.signal(signal.SIGALRM, timeout_handler)
    signal.setitimer(signal.ITIMER_REAL, timeout_seconds)

    try:
        return operation()
    finally:
        signal.setitimer(signal.ITIMER_REAL, 0)
        signal.signal(signal.SIGALRM, previous_handler)
        if previous_timer[0] > 0:
            signal.setitimer(
                signal.ITIMER_REAL,
                previous_timer[0],
                previous_timer[1],
            )


def configure_scraperapi():
    """Configure ScraperAPI as the preferred route when an API key exists."""
    api_key = (
        os.environ.get("SCRAPERAPI_KEY", "").strip()
        or os.environ.get("SCRAPER_API_KEY", "").strip()
    )
    if not api_key:
        print(
            "SCRAPERAPI_KEY is not configured; skipping ScraperAPI.",
            flush=True,
        )
        return False

    proxy_generator = ProxyGenerator()
    print("Initializing ScraperAPI proxy.", flush=True)

    try:
        proxy_ready = _run_with_alarm(
            SCRAPERAPI_SETUP_TIMEOUT,
            lambda: proxy_generator.ScraperAPI(api_key),
            "ScraperAPI initialization",
        )
    except Exception as exc:
        print(
            "ScraperAPI initialization failed: {}: {}".format(
                type(exc).__name__, exc
            ),
            file=sys.stderr,
            flush=True,
        )
        proxy_ready = False

    if not proxy_ready:
        scholarly.set_timeout(SCHOLARLY_TIMEOUT)
        print("ScraperAPI is unavailable; falling back to free proxies.", flush=True)
        return False

    # Route both primary and secondary scholarly requests through ScraperAPI.
    scholarly.use_proxy(proxy_generator, proxy_generator)
    scholarly.set_timeout(SCRAPERAPI_REQUEST_TIMEOUT)
    print("ScraperAPI configured for both scholarly request routes.", flush=True)
    return True


def configure_free_proxy():
    """Try scholarly's built-in rotating free-proxy pool with a hard time bound."""
    scholarly.set_timeout(SCHOLARLY_TIMEOUT)
    proxy_generator = ProxyGenerator()
    print(
        "Searching for a working free proxy (max {} seconds).".format(
            FREE_PROXY_SETUP_TIMEOUT
        ),
        flush=True,
    )

    try:
        proxy_ready = _run_with_alarm(
            FREE_PROXY_SETUP_TIMEOUT,
            lambda: proxy_generator.FreeProxies(
                timeout=FREE_PROXY_TIMEOUT,
                wait_time=FREE_PROXY_WAIT_TIME,
            ),
            "Free-proxy setup",
        )
    except Exception as exc:
        print(
            "Free-proxy setup failed: {}: {}".format(type(exc).__name__, exc),
            file=sys.stderr,
            flush=True,
        )
        proxy_ready = False

    if not proxy_ready:
        print("No working free proxy was configured.", flush=True)
        return False

    # Pass the same generator twice to prevent scholarly from constructing
    # another implicit FreeProxies instance for its secondary request route.
    scholarly.use_proxy(proxy_generator, proxy_generator)
    print("Free proxy configured for both scholarly request routes.", flush=True)
    return True


def configure_direct_access():
    """Use fresh, unconfigured sessions for both routes (no proxy lookup)."""
    scholarly.set_timeout(SCHOLARLY_TIMEOUT)
    direct_generator = ProxyGenerator()
    scholarly.use_proxy(direct_generator, direct_generator)
    print("Using direct access (without a proxy).", flush=True)
    return True


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
    """Try ScraperAPI, free proxies, and direct access in that order."""
    last_error = None
    routes = [
        ("ScraperAPI", configure_scraperapi),
        ("free proxy", configure_free_proxy),
        ("direct", configure_direct_access),
    ]

    for attempt in range(1, MAX_ATTEMPTS + 1):
        print("\nAttempt {}/{}:".format(attempt, MAX_ATTEMPTS), flush=True)

        for route_name, configure_route in routes:
            try:
                route_ready = configure_route()
            except Exception as setup_error:
                last_error = setup_error
                print(
                    "{} setup failed: {}: {}".format(
                        route_name,
                        type(setup_error).__name__,
                        setup_error,
                    ),
                    file=sys.stderr,
                    flush=True,
                )
                continue

            if not route_ready:
                continue

            try:
                author = fetch_full_author()
                print(
                    "Attempt {} succeeded using {} access.".format(
                        attempt, route_name
                    ),
                    flush=True,
                )
                return author
            except Exception as request_error:
                last_error = request_error
                print(
                    "{} retrieval failed: {}: {}".format(
                        route_name,
                        type(request_error).__name__,
                        request_error,
                    ),
                    file=sys.stderr,
                    flush=True,
                )
                print(
                    "Falling back to the next access method.",
                    flush=True,
                )

        if attempt < MAX_ATTEMPTS:
            print(
                "All access methods failed in this attempt. Waiting {} seconds "
                "before retrying the fallback sequence.".format(WAIT_SECONDS),
                flush=True,
            )
            time.sleep(WAIT_SECONDS)

    raise RuntimeError(
        "All {} attempts failed using ScraperAPI, free proxies, and direct access.".format(
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
