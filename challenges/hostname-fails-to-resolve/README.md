# Hostname Fails to Resolve

| Field | Value |
|-------|-------|
| **Level** | Beginner |
| **Topics** | DNS, Linux, Network Troubleshooting |
| **Base Points** | 10 |

## Description

The server can reach external IP addresses directly, but internal hostnames like
`api.internal` fail to resolve. Direct IP access works fine, so the network
itself is healthy.

## Objective

Fix the DNS resolver configuration so that `api.internal` resolves to the correct
IP address. Do not use /etc/hosts as a workaround.

## Hint

Verify /etc/resolv.conf. Is the nameserver address reachable and correct?

## How to solve (PoC)

1. Inspect: `cat /etc/resolv.conf` → check nameserver entry
2. Test: `dig api.internal` → NXDOMAIN or timeout
3. Investigate: `cat /etc/resolv.conf` → wrong nameserver IP
4. Fix: correct the nameserver address in /etc/resolv.conf
5. Verify: `dig api.internal` → resolves to correct IP

## Scoring

- Base points: 10
- Mode checker ON: full points. OFF: 0.5×.
- Bonus: without paste + high WPM.
