# Nginx pid directory missing

| Field | Value |
|-------|-------|
| **Level** | Beginner |
| **Kind** | Terminal |
| **Topics** | Nginx, Linux |
| **Checker** | ON / OFF (toggle di WebGUI) |
| **Base Points** | 10 |

## Description
Nginx fails to start because pid path directory is gone.

## Scenario
Nginx fails to start because pid path directory is gone.

## Objective
Restore the expected healthy behaviour. Symptom: Nginx fails to start because pid path directory is gone.

## Hint
Cek upstream port/path/header di nginx config. Bandingkan dengan port app yang berjalan.

## Allowed to change
_TODO: daftar file/config yang boleh diubah._

## Must NOT change
_TODO: daftar file/config yang dilarang diubah._

## How to solve (PoC)
<details>
<summary>Show solution</summary>

1. Inspect: `curl -s http://localhost:80/health` (cek status code).
2. Cek config: `cat /etc/nginx/sites-enabled/default` atau `nginx -T`.
3. Perbaiki upstream port / path / header sesuai objective.
4. Reload: `nginx -s reload` atau `systemctl reload nginx`.
5. Verifikasi: `curl -s http://localhost:80/health` → 200.
6. Verify: klik "Verify" di WebGUI → checker PASS.

</details>

## Scoring
- Base points: 10
- Mode checker ON: full points. OFF: 0.5×.
- Bonus: tanpa paste + WPM tinggi.
