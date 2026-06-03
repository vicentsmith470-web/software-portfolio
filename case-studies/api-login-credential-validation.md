# API Login Credential Validation

## Problem

The login route accepted unknown users or incorrect passwords and still returned a token. That behavior creates an authentication boundary bug because invalid credentials should not mint valid session tokens.

## Solution

The fix kept registered users in the existing in-memory auth flow so login could verify credentials before issuing a token. Unknown emails and wrong passwords now return HTTP 401, while valid registered credentials keep the successful response shape.

## Validation

- Route-level tests for unknown-user login.
- Route-level tests for wrong-password login.
- Successful login test after registration.
- Syntax checks for touched controller, service, and test files.

## Public PR

https://github.com/SecureBananaLabs/bug-bounty/pull/3467

