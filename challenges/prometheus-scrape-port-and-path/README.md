# Prometheus scrape port and path

| Field | Value |
|-------|-------|
| **Level** | Intermediate |
| **Kind** | Terminal |
| **Topics** | Prometheus, Linux |
| **Checker** | ON / OFF (toggle di WebGUI) |
| **Base Points** | 25 |

## Description
Prometheus scrapes the wrong port and metrics_path on the app sidecar. Work the workspace and sidecar as separate failure domains. A fix that only touches one container will not satisfy the end-to-end checker. Start from the participant-facing symptom, then verify each hop with curl or the service CLI until both causes are cleared.

## Scenario
Prometheus scrapes the wrong port and metrics_path on the app sidecar. Work the workspace and sidecar as separate failure domains. A fix that only touches one container will not satisfy the end-to-end checker. Start from the participant-facing symptom, then verify each hop with curl or the service CLI until both causes are cleared.

workspace

app

healthy

Click to expand

## Objective
Prometheus query ctf_up returns a value.

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
