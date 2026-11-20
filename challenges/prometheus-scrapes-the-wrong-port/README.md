# Prometheus scrapes the wrong port

| Field | Value |
|-------|-------|
| **Level** | Beginner |
| **Kind** | Terminal |
| **Topics** | Prometheus, Linux |
| **Checker** | ON / OFF (toggle di WebGUI) |
| **Base Points** | 10 |

## Description
Prometheus is running, but its scrape config points at the wrong port for the local metrics exporter. The target stays down and the expected metric never appears. Inspect `prometheus.yml`, point the scrape job at the exporter’s real listen port, reload or restart Prometheus, and confirm the metric is present via the local HTTP API.

## Scenario
Prometheus is running, but its scrape config points at the wrong port for the local metrics exporter. The target stays down and the expected metric never appears.

Inspect prometheus.yml, point the scrape job at the exporter’s real listen port, reload or restart Prometheus, and confirm the metric is present via the local HTTP API.

Prometheus

exporter :9091

metric

Click to expand

## Objective
Prometheus can scrape ctf_up from the local exporter.

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
- Base points: 10
- Mode checker ON: full points. OFF: 0.5×.
- Bonus: tanpa paste + WPM tinggi.
