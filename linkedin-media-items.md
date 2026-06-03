# LinkedIn Media Items

Use these as LinkedIn portfolio/media entries.

## API Login Credential Validation

Link: https://github.com/SecureBananaLabs/bug-bounty/pull/3467

Description:

```text
Backend Node.js/Express pull request that validates login credentials correctly. Unknown users and wrong passwords now return HTTP 401, while valid registered credentials still receive the expected token response. Includes route-level tests and validation notes.
```

## Malformed JSON Rate-Limit Fix

Link: https://github.com/SecureBananaLabs/bug-bounty/pull/3366

Description:

```text
API bug fix that ensures malformed JSON requests are counted by the global rate limiter before parser errors stop the request flow. Includes a focused regression test using a real HTTP server and documented validation commands.
```

## Reproducible PI Artifact

Link: https://github.com/SecureBananaLabs/bug-bounty/pull/3697

Description:

```text
Python reproducibility project that generates and verifies a 1,000,000-decimal PI artifact using Chudnovsky binary splitting. Includes checksum evidence, a documented artifact, and a short demo video.
```

## Freelance Proposal Tracker

Link: https://github.com/vicentsmith470-web/software-portfolio/blob/main/case-studies/freelance-proposal-tracker.md

Description:

```text
Python CLI project for tracking freelance proposals in a JSON file. It can add proposals, list active bids, and summarize estimated value by status without external dependencies.
```

## Application Log Error Summary

Link: https://github.com/vicentsmith470-web/software-portfolio/blob/main/case-studies/log-error-summary.md

Description:

```text
Python debugging utility that scans application logs, counts severity levels, and reports repeated warning/error patterns. Built as a small practical automation tool for backend maintenance work.
```

## Rule-Based File Organizer

Link: https://github.com/vicentsmith470-web/software-portfolio/blob/main/case-studies/rule-based-file-organizer.md

Description:

```text
Python automation utility that previews and applies file move/copy rules from JSON. Built for simple Windows-friendly file organization workflows with a safe dry-run mode before applying changes.
```

## Software Portfolio Repository

Link: https://github.com/vicentsmith470-web/software-portfolio

Description:

```text
Small software portfolio with API case studies, Python/Node.js utility scripts, and examples of validation-focused development work.
```
