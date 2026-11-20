# Token file unreadable by app user

| Field | Value |
|-------|-------|
| **Level** | Beginner |
| **Kind** | Terminal |
| **Topics** | Security Hardening, Linux |
| **Checker** | ON / OFF (toggle di WebGUI) |
| **Base Points** | 10 |

## Description
The application process runs as user `app` and must read `/opt/app/token`. The file exists but is not readable by that user, so the health endpoint refuses to start cleanly. Fix ownership or mode so `app` can read the token, start the health helper, and confirm the HTTP probe succeeds.

## Scenario
The application process runs as user app and must read /opt/app/token. The file exists but is not readable by that user, so the health endpoint refuses to start cleanly.

Fix ownership or mode so app can read the token, start the health helper, and confirm the HTTP probe succeeds.

user app

token file

health :9090

Click to expand

## Objective
Health endpoint on :9090 returns OK while running as app.

## Hint
Cek cert path, key mode, permission file.

## Allowed to change
_TODO: daftar file/config yang boleh diubah._

## Must NOT change
_TODO: daftar file/config yang dilarang diubah._

## How to solve (PoC)
<details>
<summary>Show solution</summary>

1. Inspect: cek cert path, key mode, permission.
2. Perbaiki path / mode / ownership sesuai objective.
3. Reload service.
4. Verifikasi: service sehat, cert valid.
5. Verify: klik "Verify" di WebGUI → checker PASS.

</details>

## Scoring
- Base points: 10
- Mode checker ON: full points. OFF: 0.5×.
- Bonus: tanpa paste + WPM tinggi.
