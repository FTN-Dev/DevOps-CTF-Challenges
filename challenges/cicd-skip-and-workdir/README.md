# Cicd Skip And Workdir

| Field | Value |
|-------|-------|
| **Level** | Intermediate |
| **Kind** | Terminal |
| **Topics** | CI/CD, Bash Scripting |
| **Checker** | ON / OFF (toggle di WebGUI) |
| **Base Points** | 25 |

## Description
A deploy step is skipped and the working directory for the remaining step is wrong.

## Scenario
A deploy step is skipped and the working directory for the remaining step is wrong.

cause A

cause B

healthy

Click to expand

## Objective
/opt/app/ci.ok contains DEPLOYED.

## Hint
Cek branch deploy dan step health check di pipeline config.

## Allowed to change
_TODO: daftar file/config yang boleh diubah._

## Must NOT change
_TODO: daftar file/config yang dilarang diubah._

## How to solve (PoC)
<details>
<summary>Show solution</summary>

1. Inspect: cek file pipeline (`.gitlab-ci.yml`, `.github/workflows/`, Jenkinsfile).
2. Cek branch: `git branch -a`, `git log --oneline`.
3. Perbaiki branch / step yang salah (health check, workdir, dll.).
4. Re-run pipeline atau service.
5. Verifikasi: `curl health endpoint` → 200.
6. Verify: klik "Verify" di WebGUI → checker PASS.

</details>

## Scoring
- Base points: 25
- Mode checker ON: full points. OFF: 0.5×.
- Bonus: tanpa paste + WPM tinggi.
