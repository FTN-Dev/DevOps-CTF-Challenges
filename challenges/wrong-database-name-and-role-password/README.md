# Wrong database name and role password

| Field | Value |
|-------|-------|
| **Level** | Intermediate |
| **Kind** | Terminal |
| **Topics** | PostgreSQL, Linux |
| **Checker** | ON / OFF (toggle di WebGUI) |
| **Base Points** | 25 |

## Description
The application stores its database name and password in `/opt/app/db.env`. Right now neither value matches the live PostgreSQL cluster: the role password is wrong, and the database the app opens does not exist. Treat this as a two-part credentials incident. Confirm the server is up, inspect the env file the app actually reads, create or rename the database the probe expects, and align the role password. Fixing only the password still leaves the probe opening a missing database; fixing only the database name still fails authentication. Walk the connection string the same way you would in production: host, port, user, password, database — one field at a time — until `SELECT 1` succeeds with the app credentials.

## Scenario
The application stores its database name and password in /opt/app/db.env. Right now neither value matches the live PostgreSQL cluster: the role password is wrong, and the database the app opens does not exist.

Treat this as a two-part credentials incident. Confirm the server is up, inspect the env file the app actually reads, create or rename the database the probe expects, and align the role password. Fixing only the password still leaves the probe opening a missing database; fixing only the database name still fails authentication.

Walk the connection string the same way you would in production: host, port, user, password, database — one field at a time — until SELECT 1 succeeds with the app credentials.

db.env

password

database

Click to expand

## Objective
App credentials in /opt/app/db.env can SELECT 1.

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
- Base points: 25
- Mode checker ON: full points. OFF: 0.5×.
- Bonus: tanpa paste + WPM tinggi.
