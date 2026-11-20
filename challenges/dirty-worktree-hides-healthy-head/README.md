# Dirty worktree hides healthy HEAD

| Field | Value |
|-------|-------|
| **Level** | Beginner |
| **Kind** | Terminal |
| **Topics** | Git, Linux |
| **Checker** | ON / OFF (toggle di WebGUI) |
| **Base Points** | 10 |

## Description
`HEAD` already contains the healthy marker, but the worktree has uncommitted edits that overwrite it with a broken value. The application reads the file from disk, so it sees the dirty content. Inspect `git status` and the file diff, restore the tracked content from `HEAD`, and confirm the on-disk marker matches the last commit.

## Scenario
HEAD already contains the healthy marker, but the worktree has uncommitted edits that overwrite it with a broken value. The application reads the file from disk, so it sees the dirty content.

Inspect git status and the file diff, restore the tracked content from HEAD, and confirm the on-disk marker matches the last commit.

healthy HEAD

dirty worktree

app reads disk

Click to expand

## Objective
Worktree STATUS matches healthy HEAD content.

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
- Base points: 10
- Mode checker ON: full points. OFF: 0.5×.
- Bonus: tanpa paste + WPM tinggi.
