# Malformed JSON Rate-Limit Behavior

## Problem

Malformed JSON requests could hit the API parser before the global rate limiter counted them. Repeated malformed requests should still be counted by rate limiting instead of bypassing the limiter through parser errors.

## Solution

The fix moved the global API rate limiter before JSON body parsing. This keeps normal request behavior intact while ensuring malformed JSON traffic is counted before parser errors short-circuit the request stack.

## Validation

- Regression test using a real ephemeral HTTP server.
- Repeated malformed JSON requests eventually return HTTP 429.
- Syntax checks and diff checks on touched files.

## Public PR

https://github.com/SecureBananaLabs/bug-bounty/pull/3366

