# Obs Port And Path

| Field | Value |
|-------|-------|
| **Level** | Intermediate |
| **Kind** | Terminal |
| **Topics** | Prometheus, Linux |
| **Checker** | ON / OFF (toggle di WebGUI) |
| **Base Points** | 25 |

## Description
Prometheus scrapes the wrong port and the wrong metrics_path.

## Scenario
Prometheus scrapes the wrong port and the wrong metrics_path.

cause A

cause B

healthy

Click to expand

## Objective
Query ctf_up returns a value.

## Hint
Cek konfigurasi yang relevan dengan objective. Identifikasi apa yang salah.

## Allowed to change
_TODO: daftar file/config yang boleh diubah._

## Must NOT change
_TODO: daftar file/config yang dilarang diubah._

## How to solve (PoC)
<details>
<summary>Show solution</summary>

1. Inspect: `curl localhost:9090/targets` atau cek config.
2. Cek scrape port / metrics_path / sidecar.
3. Perbaiki config Prometheus sesuai objective.
4. Reload: `kill -HUP $(pidof prometheus)` atau restart.
5. Verifikasi: target UP di Prometheus UI.
6. Verify: klik "Verify" di WebGUI → checker PASS.

</details>

## Scoring
- Base points: 25
- Mode checker ON: full points. OFF: 0.5×.
- Bonus: tanpa paste + WPM tinggi.
