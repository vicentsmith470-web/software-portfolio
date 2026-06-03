# Application Log Error Summary

## Problem

Debugging logs manually is slow when a file contains repeated warnings and errors. A quick summary helps identify the most common failure patterns before opening the code.

## Solution

This portfolio includes a small Python CLI that scans plain-text logs, counts messages by severity, and reports the most repeated warning/error lines.

## Validation

- Parses `examples/sample_app.log`.
- Counts `INFO`, `WARN`, and `ERROR` lines.
- Reports the top repeated warning/error messages.
- Uses only the Python standard library.

## Sample Command

```bash
python tools/log_error_summary.py examples/sample_app.log
```

