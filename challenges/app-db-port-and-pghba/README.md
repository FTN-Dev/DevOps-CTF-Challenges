# App DB port and pg_hba

| Field | Value |
|-------|-------|
| **Level** | Intermediate |
| **Kind** | Terminal |
| **Topics** | PostgreSQL, Linux |
| **Checker** | ON / OFF (toggle di WebGUI) |
| **Base Points** | 25 |

## Description
The app connection string uses the wrong port and the database sidecar rejects the role in pg_hba. Work the workspace and sidecar as separate failure domains. A fix that only touches one container will not satisfy the end-to-end checker. Start from the participant-facing symptom, then verify each hop with curl or the service CLI until both causes are cleared.

## Scenario
The app connection string uses the wrong port and the database sidecar rejects the role in pg_hba. Work the workspace and sidecar as separate failure domains. A fix that only touches one container will not satisfy the end-to-end checker. Start from the participant-facing symptom, then verify each hop with curl or the service CLI until both causes are cleared.

workspace

db

healthy

Click to expand

## Objective
App health endpoint returns OK.

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
