# Prometheus rule file not loaded

| Field | Value |
|-------|-------|
| **Level** | Beginner |
| **Kind** | Terminal |
| **Topics** | Prometheus, Linux |
| **Checker** | ON / OFF (toggle di WebGUI) |
| **Base Points** | 10 |

## Description
Prometheus scrapes successfully, but the alerting/recording rule file that defines `ctf_ready` is not loaded because the rule_files path is wrong. Queries for that recording rule return empty. Point `rule_files` at the real rule file, restart Prometheus, wait for evaluation, and confirm the recording rule appears.

## Scenario
Prometheus scrapes successfully, but the alerting/recording rule file that defines ctf_ready is not loaded because the rule_files path is wrong. Queries for that recording rule return empty.

Point rule_files at the real rule file, restart Prometheus, wait for evaluation, and confirm the recording rule appears.

Prometheus

rule_files

ctf_ready

Click to expand

## Objective
Recording rule ctf_ready is queryable.

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
