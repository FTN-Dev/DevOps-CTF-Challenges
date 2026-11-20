# Redis bind and port both wrong

| Field | Value |
|-------|-------|
| **Level** | Intermediate |
| **Kind** | Terminal |
| **Topics** | Redis, Linux |
| **Checker** | ON / OFF (toggle di WebGUI) |
| **Base Points** | 25 |

## Description
Redis is running, but the application cannot reach it. Two independent mistakes are present in the server configuration: the process listens on an unexpected port, and it binds to an address the client does not use. Open the Redis config under `/opt/redis`, correct both `port` and `bind`, restart the daemon, and confirm `PING` from the documented client settings. Changing only the port still leaves the bind unreachable; changing only the bind still leaves the client talking to the wrong port. This mirrors production cache outages where `ss`/`curl` look “half right” until every listener field matches the client.

## Scenario
Redis is running, but the application cannot reach it. Two independent mistakes are present in the server configuration: the process listens on an unexpected port, and it binds to an address the client does not use.

Open the Redis config under /opt/redis, correct both port and bind, restart the daemon, and confirm PING from the documented client settings. Changing only the port still leaves the bind unreachable; changing only the bind still leaves the client talking to the wrong port.

This mirrors production cache outages where ss/curl look “half right” until every listener field matches the client.

redis.conf

bind

port

Click to expand

## Objective
redis-cli -p 6379 PING returns PONG on 127.0.0.1.

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
