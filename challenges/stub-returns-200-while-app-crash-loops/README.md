# Stub returns 200 while app crash-loops

| Field | Value |
|-------|-------|
| **Level** | Beginner |
| **Kind** | Terminal |
| **Topics** | Linux |
| **Checker** | ON / OFF (toggle di WebGUI) |
| **Base Points** | 10 |

## Description
Stub answers OK-looking 200 with STUB; real app dies immediately.

## Scenario
Stub answers OK-looking 200 with STUB; real app dies immediately.

## Objective
Restore the expected healthy behaviour. Symptom: Stub answers OK-looking 200 with STUB; real app dies immediately.

## Hint
Cek service/process/config yang relevan. Identifikasi misconfig.

## Allowed to change
_TODO: daftar file/config yang boleh diubah._

## Must NOT change
_TODO: daftar file/config yang dilarang diubah._

## How to solve (PoC)
<details>
<summary>Show solution</summary>

1. Inspect: cek service/process/config yang relevan.
2. Identifikasi misconfig (port, permission, path, user).
3. Perbaiki sesuai objective.
4. Restart service jika perlu.
5. Verifikasi: health check / command test.
6. Verify: klik "Verify" di WebGUI → checker PASS.

</details>

## Scoring
- Base points: 10
- Mode checker ON: full points. OFF: 0.5×.
- Bonus: tanpa paste + WPM tinggi.
