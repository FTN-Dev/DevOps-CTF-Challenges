# Web Server Refuses to Start

| Field | Value |
|-------|-------|
| **Level** | Beginner |
| **Topics** | Linux, Nginx |
| **Base Points** | 10 |

## Description

An internal web service was working fine until a configuration change was applied.
Now Nginx refuses to start and the site is completely down. No error details are
shown to end users.

## Objective

Fix the Nginx configuration so the web server starts successfully and serves
content on port 80.

## Hint

Run `nginx -t` to see the syntax error location and details.

## How to solve (PoC)

1. Inspect: `systemctl status nginx` → failed to start
2. Investigate: `nginx -t` → syntax error with line number
3. Fix: correct the missing bracket/semicolon in the config file
4. Verify: `nginx -t` → syntax ok
5. Confirm: `curl http://localhost/` returns the expected page

## Scoring

- Base points: 10
- Mode checker ON: full points. OFF: 0.5×.
- Bonus: without paste + high WPM.
