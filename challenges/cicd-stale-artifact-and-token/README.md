# Cicd Stale Artifact And Token

| Field | Value |
|-------|-------|
| **Level** | Intermediate |
| **Kind** | Terminal |
| **Topics** | CI/CD, Bash Scripting |
| **Checker** | ON / OFF (toggle di WebGUI) |
| **Base Points** | 25 |

## Description
The pipeline deploys a stale artifact and never exports the required token env. Investigate both failure modes independently: correcting only one still leaves the checker red. Use the station files under `/opt` as the system of record, apply a minimal fix for each cause, then re-run the service or playbook the scenario depends on. Author notes (hidden from participants) encode the exact pair: stale + env.

## Scenario
The pipeline deploys a stale artifact and never exports the required token env. Investigate both failure modes independently: correcting only one still leaves the checker red. Use the station files under /opt as the system of record, apply a minimal fix for each cause, then re-run the service or playbook the scenario depends on. Author notes (hidden from participants) encode the exact pair: stale + env.

cause A

cause B

healthy

Click to expand

## Objective
/opt/app/ci.ok contains DEPLOYED and TOKEN is present.

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
