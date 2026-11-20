# Ssh Pubkey And Perm

| Field | Value |
|-------|-------|
| **Level** | Intermediate |
| **Kind** | Terminal |
| **Topics** | Linux, Security Hardening |
| **Checker** | ON / OFF (toggle di WebGUI) |
| **Base Points** | 25 |

## Description
PubkeyAuthentication is disabled and ~/.ssh permissions are too open. Both block key login. Investigate both failure modes independently: correcting only one still leaves the checker red. Use the station files under `/opt` as the system of record, apply a minimal fix for each cause, then re-run the service or playbook the scenario depends on. Author notes (hidden from participants) encode the exact pair: PubkeyAuthentication no + mode 0777.

## Scenario
PubkeyAuthentication is disabled and ~/.ssh permissions are too open. Both block key login. Investigate both failure modes independently: correcting only one still leaves the checker red. Use the station files under /opt as the system of record, apply a minimal fix for each cause, then re-run the service or playbook the scenario depends on. Author notes (hidden from participants) encode the exact pair: PubkeyAuthentication no + mode 0777.

cause A

cause B

healthy

Click to expand

## Objective
Key-based SSH as ctf on 2222 succeeds.

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
- Base points: 25
- Mode checker ON: full points. OFF: 0.5×.
- Bonus: tanpa paste + WPM tinggi.
