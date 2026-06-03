# Software Portfolio

Small, practical software work focused on API fixes, automation, testing, and technical documentation.

## Focus

- JavaScript and Node.js API fixes
- Python automation scripts
- REST API validation
- Bug reproduction and regression tests
- GitHub pull requests with clear validation evidence
- Technical documentation and reproducible artifacts

## Case Studies

- [API login credential validation](case-studies/api-login-credential-validation.md)
- [Malformed JSON rate-limit behavior](case-studies/malformed-json-rate-limit.md)
- [Reproducible PI artifact and verifier](case-studies/reproducible-pi-artifact.md)
- [Freelance proposal tracker](case-studies/freelance-proposal-tracker.md)
- [Application log error summary](case-studies/log-error-summary.md)
- [Rule-based file organizer](case-studies/rule-based-file-organizer.md)

## Sample Tools

- [API status checker](tools/api_status_checker.py): dependency-free Python script for checking endpoint health and response timing.
- [JSON payload validator](tools/json_payload_validator.js): dependency-free Node.js CLI for validating JSON files before sending them to APIs.
- [Freelance proposal tracker](tools/proposal_tracker.py): dependency-free Python CLI for tracking bids, values, and statuses.
- [Log error summary](tools/log_error_summary.py): dependency-free Python CLI for summarizing application log warnings and errors.
- [Rule-based file organizer](tools/file_rule_mover.py): dependency-free Python CLI for previewing and applying file move/copy rules.

## Validation Commands

```bash
python -m py_compile tools/api_status_checker.py tools/proposal_tracker.py tools/log_error_summary.py tools/file_rule_mover.py
node --check tools/json_payload_validator.js
python tools/proposal_tracker.py --store examples/proposals.sample.json summary
python tools/log_error_summary.py examples/sample_app.log
python tools/file_rule_mover.py examples/file_rules.sample.json
node tools/json_payload_validator.js examples/proposals.sample.json
```

## Recent Public Work

- Login credential validation PR: https://github.com/SecureBananaLabs/bug-bounty/pull/3467
- Malformed JSON rate-limit PR: https://github.com/SecureBananaLabs/bug-bounty/pull/3366
- Reproducible PI artifact PR: https://github.com/SecureBananaLabs/bug-bounty/pull/3697
