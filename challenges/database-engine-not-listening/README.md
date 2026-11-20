# Database Engine Not Listening

| Field | Value |
|-------|-------|
| **Level** | Beginner |
| **Topics** | PostgreSQL, Linux |
| **Base Points** | 10 |

## Description

The application health check talks to a local PostgreSQL instance and expects a
successful query. The database process is not listening, so clients fail immediately
when they try to connect.

## Objective

Start the PostgreSQL server with the prepared data directory and verify that a
simple SELECT 1 query succeeds against the local socket.

## Hint

Is the database process actually running? Check with pgrep or ss before blaming
credentials or application code.

## How to solve (PoC)

1. Inspect: `pgrep postgres` → no process found
2. Investigate: `ss -tlnp | grep 5432` → no listener
3. Check: `ls /var/lib/postgresql/data/` → data directory exists
4. Fix: start PostgreSQL with `pg_ctl start -D /var/lib/postgresql/data`
5. Verify: `psql -U postgres -c "SELECT 1;"` → returns 1

## Scoring

- Base points: 10
- Mode checker ON: full points. OFF: 0.5×.
- Bonus: without paste + high WPM.
