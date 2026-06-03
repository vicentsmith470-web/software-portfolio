#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import time
import urllib.error
import urllib.request


def check_url(url: str, timeout: float) -> dict[str, object]:
    started = time.perf_counter()
    try:
        with urllib.request.urlopen(url, timeout=timeout) as response:
            body = response.read(1024)
            elapsed_ms = round((time.perf_counter() - started) * 1000, 2)
            return {
                "url": url,
                "ok": 200 <= response.status < 400,
                "status": response.status,
                "elapsed_ms": elapsed_ms,
                "sample_bytes": len(body),
            }
    except urllib.error.HTTPError as error:
        elapsed_ms = round((time.perf_counter() - started) * 1000, 2)
        return {
            "url": url,
            "ok": False,
            "status": error.code,
            "elapsed_ms": elapsed_ms,
            "error": error.reason,
        }
    except Exception as error:
        elapsed_ms = round((time.perf_counter() - started) * 1000, 2)
        return {
            "url": url,
            "ok": False,
            "status": None,
            "elapsed_ms": elapsed_ms,
            "error": str(error),
        }


def main() -> int:
    parser = argparse.ArgumentParser(description="Check HTTP endpoint status and response time.")
    parser.add_argument("urls", nargs="+", help="One or more URLs to check.")
    parser.add_argument("--timeout", type=float, default=10.0, help="Request timeout in seconds.")
    args = parser.parse_args()

    results = [check_url(url, args.timeout) for url in args.urls]
    print(json.dumps(results, indent=2))
    return 0 if all(result["ok"] for result in results) else 1


if __name__ == "__main__":
    raise SystemExit(main())

