# pg_hba rejects the app role

| Field | Value |
|-------|-------|
| **Level** | Beginner |
| **Kind** | Terminal |
| **Topics** | PostgreSQL, Security Hardening |
| **Checker** | ON / OFF (toggle di WebGUI) |
| **Base Points** | 10 |

## Description
PostgreSQL is up, but the application role is rejected by host-based authentication. Connection attempts fail with an authentication / pg_hba style error rather than a missing process. Review `pg_hba.conf` for the local connection path the app uses, reload or restart so the rule takes effect, and verify the app role can connect. Keep trust-vs-reject rules intentional: the healthy rule must allow the application role over the local socket.

## Scenario
PostgreSQL is up, but the application role is rejected by host-based authentication. Connection attempts fail with an authentication / pg_hba style error rather than a missing process.

Review pg_hba.conf for the local connection path the app uses, reload or restart so the rule takes effect, and verify the app role can connect. Keep trust-vs-reject rules intentional: the healthy rule must allow the application role over the local socket.

allow

App role

pg_hba.conf

Database

Click to expand

## Objective
Role app can run SELECT 1 over the local socket.

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
