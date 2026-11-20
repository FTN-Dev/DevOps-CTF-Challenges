# Git Branch And Gitignore

| Field | Value |
|-------|-------|
| **Level** | Intermediate |
| **Kind** | Terminal |
| **Topics** | Git, Linux |
| **Checker** | ON / OFF (toggle di WebGUI) |
| **Base Points** | 25 |

## Description
The worktree is on the wrong branch and .gitignore hides the file the app reads.

## Scenario
The worktree is on the wrong branch and .gitignore hides the file the app reads.

cause A

cause B

healthy

Click to expand

## Objective
/opt/app/repo/STATUS is HEALTHY and tracked.

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
