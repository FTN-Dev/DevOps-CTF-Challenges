# Terraform HCL fails validate

| Field | Value |
|-------|-------|
| **Level** | Beginner |
| **Kind** | Terminal |
| **Topics** | Terraform, Linux |
| **Checker** | ON / OFF (toggle di WebGUI) |
| **Base Points** | 10 |

## Description
A local Terraform root module fails `terraform validate` because of broken HCL syntax. Until validation passes, the intended `local_file` resource cannot be applied safely. Open the module under `/opt/tf`, repair the syntax error, run `terraform init` if needed, validate, and apply so the output file appears with the healthy content.

## Scenario
A local Terraform root module fails terraform validate because of broken HCL syntax. Until validation passes, the intended local_file resource cannot be applied safely.

Open the module under /opt/tf, repair the syntax error, run terraform init if needed, validate, and apply so the output file appears with the healthy content.

main.tf

validate

local_file

Click to expand

## Objective
/opt/app/tf.out exists with content ok after a successful apply.

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
- Base points: 10
- Mode checker ON: full points. OFF: 0.5×.
- Bonus: tanpa paste + WPM tinggi.
