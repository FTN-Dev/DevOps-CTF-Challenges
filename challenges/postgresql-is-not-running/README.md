# PostgreSQL is not running

| Field | Value |
|-------|-------|
| **Level** | Beginner |
| **Kind** | Terminal |
| **Topics** | PostgreSQL, Linux |
| **Checker** | ON / OFF (toggle di WebGUI) |
| **Base Points** | 10 |

## Description
The application health check talks to a local PostgreSQL instance and expects a successful query. Right now the database process is not listening, so clients fail immediately when they try to connect. Start by confirming whether the PostgreSQL server process is alive and whether a socket or TCP listener exists on the usual local port. Check process listings and any startup logs under `/tmp` or the data directory. The healthy path is: start the server with the prepared data directory, then verify a simple `SELECT 1` against the local socket. This station teaches the first question in every database incident: is the engine actually running before you blame credentials, schemas, or application code?

## Scenario
The application health check talks to a local PostgreSQL instance and expects a successful query. Right now the database process is not listening, so clients fail immediately when they try to connect.

Start by confirming whether the PostgreSQL server process is alive and whether a socket or TCP listener exists on the usual local port. Check process listings and any startup logs under /tmp or the data directory. The healthy path is: start the server with the prepared data directory, then verify a simple SELECT 1 against the local socket.

This station teaches the first question in every database incident: is the engine actually running before you blame credentials, schemas, or application code?

App health

PostgreSQL

SELECT 1

Click to expand

## Objective
PostgreSQL accepts a local SELECT 1 query.

## Hint
Cek port di postgresql.conf dan role di pg_hba.conf. Pastikan app connection string sesuai.

## Allowed to change
_TODO: daftar file/config yang boleh diubah._

## Must NOT change
_TODO: daftar file/config yang dilarang diubah._

## How to solve (PoC)
<details>
<summary>Show solution</summary>

1. Inspect: `psql -U postgres -c '\conninfo'` atau `pg_isready`.
2. Cek port: `ss -tlnp | grep postgres` atau config `postgresql.conf`.
3. Cek pg_hba: `cat /etc/postgresql/*/main/pg_hba.conf`.
4. Perbaiki port / pg_hba sesuai objective.
5. Reload: `pg_ctl reload` atau restart service.
6. Verifikasi: `psql -h localhost -p <port> -U <role> -c 'SELECT 1'`.
7. Verify: klik "Verify" di WebGUI → checker PASS.

</details>

## Scoring
- Base points: 10
- Mode checker ON: full points. OFF: 0.5×.
- Bonus: tanpa paste + WPM tinggi.
