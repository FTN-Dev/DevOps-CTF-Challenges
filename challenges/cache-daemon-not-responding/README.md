# Cache Daemon Not Responding

| Field | Value |
|-------|-------|
| **Level** | Beginner |
| **Topics** | Redis, Linux |
| **Base Points** | 10 |

## Description

The cache layer is supposed to answer PING with PONG on the local Redis port.
The process is down, so every cache read fails fast and the application
cannot retrieve cached data.

## Objective

Start the Redis server with the prepared configuration and verify that
PING returns PONG.

## Hint

Is the Redis daemon actually running? Check the process list and port binding
before investigating authentication or configuration issues.

## How to solve (PoC)

1. Inspect: `pgrep redis` → no process found
2. Investigate: `ss -tlnp | grep 6379` → no listener
3. Check: `ls /opt/redis/redis.conf` → config exists
4. Fix: start Redis with `redis-server /opt/redis/redis.conf`
5. Verify: `redis-cli PING` → PONG

## Scoring

- Base points: 10
- Mode checker ON: full points. OFF: 0.5×.
- Bonus: without paste + high WPM.
