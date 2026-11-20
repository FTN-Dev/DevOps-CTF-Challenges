# Config symlink points at the wrong file

| Field | Value |
|-------|-------|
| **Level** | Beginner |
| **Kind** | Terminal |
| **Topics** | Git, Linux |
| **Checker** | ON / OFF (toggle di WebGUI) |
| **Base Points** | 10 |

## Description
The application loads `/opt/app/config.env` through a symlink. The link currently points at a broken file, while the healthy configuration sits next to it under a different name. Inspect the symlink target, repoint it to the healthy file, and confirm the application marker derived from that config is correct.

## Scenario
The application loads /opt/app/config.env through a symlink. The link currently points at a broken file, while the healthy configuration sits next to it under a different name.

Inspect the symlink target, repoint it to the healthy file, and confirm the application marker derived from that config is correct.

app

config.env symlink

config.env.ok

Click to expand

## Objective
/opt/app/config.env resolves to content MODE=ok.

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
