# Redis password and DB index mismatch

| Field | Value |
|-------|-------|
| **Level** | Intermediate |
| **Kind** | Terminal |
| **Topics** | Redis, Linux |
| **Checker** | ON / OFF (toggle di WebGUI) |
| **Base Points** | 25 |

## Description
The cache client authenticates with the wrong password and then reads the wrong Redis logical database. The marker key only appears when both the secret and the DB index match the server.

## Scenario
The cache client authenticates with the wrong password and then reads the wrong Redis logical database. The marker key only appears when both the secret and the DB index match the server.

client

password

SELECT n

Click to expand

## Objective
GET marker returns ok using /opt/app/redis.env.

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
