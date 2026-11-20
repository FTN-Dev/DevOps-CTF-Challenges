# CI writes the marker in the wrong directory

| Field | Value |
|-------|-------|
| **Level** | Beginner |
| **Kind** | Terminal |
| **Topics** | CI/CD, Bash Scripting |
| **Checker** | ON / OFF (toggle di WebGUI) |
| **Base Points** | 10 |

## Description
The CI pipeline writes the healthy marker, but into the wrong working directory. The application and checker look under `/opt/app`, while the script `cd`s elsewhere before writing. Correct the working directory (or the destination path), re-run the pipeline, and verify the marker lands where the app expects it.

## Scenario
The CI pipeline writes the healthy marker, but into the wrong working directory. The application and checker look under /opt/app, while the script cds elsewhere before writing.

Correct the working directory (or the destination path), re-run the pipeline, and verify the marker lands where the app expects it.

fixed

run.sh

/tmp

/opt/app

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
- Base points: 10
- Mode checker ON: full points. OFF: 0.5×.
- Bonus: tanpa paste + WPM tinggi.
