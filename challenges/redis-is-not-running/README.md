# Redis is not running

| Field | Value |
|-------|-------|
| **Level** | Beginner |
| **Kind** | Terminal |
| **Topics** | Redis, Linux |
| **Checker** | ON / OFF (toggle di WebGUI) |
| **Base Points** | 10 |

## Description
The cache layer is supposed to answer `PING` with `PONG` on the local Redis port. The process is down, so every cache read fails fast. Confirm Redis is not running, inspect the prepared config under `/opt/redis`, start the server with that config, and re-check `PING`. This is the same “is the daemon up?” habit as with PostgreSQL, applied to an in-memory store.

## Scenario
The cache layer is supposed to answer PING with PONG on the local Redis port. The process is down, so every cache read fails fast.

Confirm Redis is not running, inspect the prepared config under /opt/redis, start the server with that config, and re-check PING. This is the same “is the daemon up?” habit as with PostgreSQL, applied to an in-memory store.

App

Redis

PONG

Click to expand

## Objective
redis-cli PING returns PONG.

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
