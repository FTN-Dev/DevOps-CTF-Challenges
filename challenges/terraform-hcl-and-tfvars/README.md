# Terraform Hcl And Tfvars

| Field | Value |
|-------|-------|
| **Level** | Intermediate |
| **Kind** | Terminal |
| **Topics** | Terraform, Linux |
| **Checker** | ON / OFF (toggle di WebGUI) |
| **Base Points** | 25 |

## Description
HCL is invalid and the active tfvars file is not the one participants notice first.

## Scenario
HCL is invalid and the active tfvars file is not the one participants notice first.

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
