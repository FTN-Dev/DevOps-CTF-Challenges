# Redis password mismatch

| Field | Value |
|-------|-------|
| **Level** | Beginner |
| **Kind** | Terminal |
| **Topics** | Redis, Security Hardening |
| **Checker** | ON / OFF (toggle di WebGUI) |
| **Base Points** | 10 |

## Description
Redis requires authentication, but the application sends a password that does not match `requirepass`. Unauthenticated commands fail; authenticated ones with the wrong secret also fail. Inspect the Redis configuration for the expected password, align the client secret used by the probe/app helper, and confirm `PING` succeeds after `AUTH`. Do not disable authentication entirely unless the scenario’s healthy state requires it.

## Scenario
Redis requires authentication, but the application sends a password that does not match requirepass. Unauthenticated commands fail; authenticated ones with the wrong secret also fail.

Inspect the Redis configuration for the expected password, align the client secret used by the probe/app helper, and confirm PING succeeds after AUTH. Do not disable authentication entirely unless the scenario’s healthy state requires it.

App AUTH

requirepass

PING

Click to expand

## Objective
Authenticated PING succeeds with the application password file.

## Hint
Cek port dan requirepass di redis.conf. Pastikan app pakai port/password yang sama.

## Allowed to change
_TODO: daftar file/config yang boleh diubah._

## Must NOT change
_TODO: daftar file/config yang dilarang diubah._

## How to solve (PoC)
<details>
<summary>Show solution</summary>

1. Inspect: `redis-cli -p <port> ping` atau `redis-cli -a <pass> ping`.
2. Cek port & password: `grep -E 'port|requirepass' /etc/redis/redis.conf`.
3. Perbaiki port / requirepass sesuai objective.
4. Restart: `redis-cli shutdown` lalu `redis-server /etc/redis/redis.conf`.
5. Verifikasi: `redis-cli -p <port> -a <pass> ping` → PONG.
6. Verify: klik "Verify" di WebGUI → checker PASS.

</details>

## Scoring
- Base points: 10
- Mode checker ON: full points. OFF: 0.5×.
- Bonus: tanpa paste + WPM tinggi.
