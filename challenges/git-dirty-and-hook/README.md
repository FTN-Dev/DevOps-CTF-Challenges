# Git Dirty And Hook

| Field | Value |
|-------|-------|
| **Level** | Intermediate |
| **Kind** | Terminal |
| **Topics** | Git, Linux |
| **Checker** | ON / OFF (toggle di WebGUI) |
| **Base Points** | 25 |

## Description
The worktree overwrites a healthy commit and a broken hook interpreter blocks restore workflows. Investigate both failure modes independently: correcting only one still leaves the checker red. Use the station files under `/opt` as the system of record, apply a minimal fix for each cause, then re-run the service or playbook the scenario depends on. Author notes (hidden from participants) encode the exact pair: dirty + bad hook shebang.

## Scenario
The worktree overwrites a healthy commit and a broken hook interpreter blocks restore workflows. Investigate both failure modes independently: correcting only one still leaves the checker red. Use the station files under /opt as the system of record, apply a minimal fix for each cause, then re-run the service or playbook the scenario depends on. Author notes (hidden from participants) encode the exact pair: dirty + bad hook shebang.

cause A

cause B

healthy

Click to expand

## Objective
STATUS is HEALTHY and the pre-commit hook is executable with a valid interpreter.

## Hint
Cek git status, branch, hook, .gitignore. Ada yang salah?

## Allowed to change
_TODO: daftar file/config yang boleh diubah._

## Must NOT change
_TODO: daftar file/config yang dilarang diubah._

## How to solve (PoC)
<details>
<summary>Show solution</summary>

1. Inspect: `git status`, `git log --oneline`, `git diff`.
2. Cek file yang salah (dirty, hook, branch, .gitignore).
3. Perbaiki sesuai objective.
4. Verifikasi: `git status` clean, hook berjalan.
5. Verify: klik "Verify" di WebGUI → checker PASS.

</details>

## Scoring
- Base points: 25
- Mode checker ON: full points. OFF: 0.5×.
- Bonus: tanpa paste + WPM tinggi.
