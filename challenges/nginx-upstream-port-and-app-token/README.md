# Nginx upstream port and app token

| Field | Value |
|-------|-------|
| **Level** | Intermediate |
| **Kind** | Terminal |
| **Topics** | Nginx, Linux |
| **Checker** | ON / OFF (toggle di WebGUI) |
| **Base Points** | 25 |

## Description
Nginx proxies to the wrong upstream port while the app rejects the token header. Both containers must be healthy.

## Scenario
Nginx proxies to the wrong upstream port while the app rejects the token header. Both containers must be healthy.

workspace

app

healthy

Click to expand

## Objective
curl through nginx returns OK.

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
- Base points: 25
- Mode checker ON: full points. OFF: 0.5×.
- Bonus: tanpa paste + WPM tinggi.
