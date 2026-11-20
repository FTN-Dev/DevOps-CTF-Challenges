# Terraform writes the wrong output path

| Field | Value |
|-------|-------|
| **Level** | Beginner |
| **Kind** | Terminal |
| **Topics** | Terraform, Linux |
| **Checker** | ON / OFF (toggle di WebGUI) |
| **Base Points** | 10 |

## Description
Terraform validates and applies, but the `local_file` resource writes to the wrong path. The checker looks for the healthy file in the documented location. Update the resource filename (or move the result) so the expected path contains the healthy content, then re-apply.

## Scenario
Terraform validates and applies, but the local_file resource writes to the wrong path. The checker looks for the healthy file in the documented location.

Update the resource filename (or move the result) so the expected path contains the healthy content, then re-apply.

fixed

local_file

wrong path

/opt/app/tf.out

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
- Base points: 10
- Mode checker ON: full points. OFF: 0.5×.
- Bonus: tanpa paste + WPM tinggi.
