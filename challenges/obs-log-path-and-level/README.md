# Obs Log Path And Level

| Field | Value |
|-------|-------|
| **Level** | Intermediate |
| **Kind** | Terminal |
| **Topics** | Log Analysis, Linux |
| **Checker** | ON / OFF (toggle di WebGUI) |
| **Base Points** | 25 |

## Description
The log shipper reads the wrong path and filters out the required level field. Investigate both failure modes independently: correcting only one still leaves the checker red. Use the station files under `/opt` as the system of record, apply a minimal fix for each cause, then re-run the service or playbook the scenario depends on. Author notes (hidden from participants) encode the exact pair: path + level filter.

## Scenario
The log shipper reads the wrong path and filters out the required level field. Investigate both failure modes independently: correcting only one still leaves the checker red. Use the station files under /opt as the system of record, apply a minimal fix for each cause, then re-run the service or playbook the scenario depends on. Author notes (hidden from participants) encode the exact pair: path + level filter.

cause A

cause B

healthy

Click to expand

## Objective
/opt/app/obs.ok contains READY from the parsed log.

## Hint
Cek konfigurasi yang relevan dengan objective. Identifikasi apa yang salah.

## Allowed to change
_TODO: daftar file/config yang boleh diubah._

## Must NOT change
_TODO: daftar file/config yang dilarang diubah._

## How to solve (PoC)
<details>
<summary>Show solution</summary>

1. Inspect: cek log file path & level.
2. Perbaiki config sesuai objective.
3. Restart service.
4. Verifikasi: log muncul di path yang benar.
5. Verify: klik "Verify" di WebGUI → checker PASS.

</details>

## Scoring
- Base points: 25
- Mode checker ON: full points. OFF: 0.5×.
- Bonus: tanpa paste + WPM tinggi.
