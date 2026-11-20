# PostgreSQL listens on the wrong port

| Field | Value |
|-------|-------|
| **Level** | Beginner |
| **Kind** | Terminal |
| **Topics** | PostgreSQL, Linux |
| **Checker** | ON / OFF (toggle di WebGUI) |
| **Base Points** | 10 |

## Description
Clients expect PostgreSQL on the standard local port, but the server was started on a different listen port. Connection attempts to the expected port get refused even though the process is running. Inspect the running configuration and any `-p` / `port` settings used when the server was started. Bring the listener back to the expected port without changing credentials. Confirm with a client that connects to the standard port.

## Scenario
Clients expect PostgreSQL on the standard local port, but the server was started on a different listen port. Connection attempts to the expected port get refused even though the process is running.

Inspect the running configuration and any -p / port settings used when the server was started. Bring the listener back to the expected port without changing credentials. Confirm with a client that connects to the standard port.

refused

psql :5432

Listener elsewhere

Listener :5432

Click to expand

## Objective
PostgreSQL accepts connections on port 5432.

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
