# Terraform Path And Count

| Field | Value |
|-------|-------|
| **Level** | Intermediate |
| **Kind** | Terminal |
| **Topics** | Terraform, Linux |
| **Checker** | ON / OFF (toggle di WebGUI) |
| **Base Points** | 25 |

## Description
local_file writes the wrong path and count evaluates to zero. Investigate both failure modes independently: correcting only one still leaves the checker red. Use the station files under `/opt` as the system of record, apply a minimal fix for each cause, then re-run the service or playbook the scenario depends on. Author notes (hidden from participants) encode the exact pair: path + count=0.

## Scenario
local_file writes the wrong path and count evaluates to zero. Investigate both failure modes independently: correcting only one still leaves the checker red. Use the station files under /opt as the system of record, apply a minimal fix for each cause, then re-run the service or playbook the scenario depends on. Author notes (hidden from participants) encode the exact pair: path + count=0.

cause A

cause B

healthy

Click to expand

## Objective
/opt/app/tf.out contains ok.

## Hint
Cek konfigurasi yang relevan dengan objective. Identifikasi apa yang salah.

## Allowed to change
_TODO: daftar file/config yang boleh diubah._

## Must NOT change
_TODO: daftar file/config yang dilarang diubah._

## How to solve (PoC)
<details>
<summary>Show solution</summary>

1. Inspect: `terraform plan` atau `terraform validate`.
2. Cek path / count / hcl / tfvars.
3. Perbaiki konfigurasi sesuai objective.
4. Apply: `terraform apply -auto-approve` (jika perlu).
5. Verifikasi: `terraform plan` → no changes.
6. Verify: klik "Verify" di WebGUI → checker PASS.

</details>

## Scoring
- Base points: 25
- Mode checker ON: full points. OFF: 0.5×.
- Bonus: tanpa paste + WPM tinggi.
