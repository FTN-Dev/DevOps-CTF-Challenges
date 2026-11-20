# App Redis port and password

| Field | Value |
|-------|-------|
| **Level** | Intermediate |
| **Kind** | Terminal |
| **Topics** | Redis, Linux |
| **Checker** | ON / OFF (toggle di WebGUI) |
| **Base Points** | 25 |

## Description
The app talks to the wrong Redis port and the requirepass does not match.

## Scenario
The app talks to the wrong Redis port and the requirepass does not match.

workspace

cache

healthy

Click to expand

## Objective
App health endpoint returns OK.

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
- Base points: 25
- Mode checker ON: full points. OFF: 0.5×.
- Bonus: tanpa paste + WPM tinggi.
