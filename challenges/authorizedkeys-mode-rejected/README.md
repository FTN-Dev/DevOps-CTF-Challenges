# authorized_keys mode rejected

| Field | Value |
|-------|-------|
| **Level** | Beginner |
| **Kind** | Terminal |
| **Topics** | Linux, Security Hardening |
| **Checker** | ON / OFF (toggle di WebGUI) |
| **Base Points** | 10 |

## Description
`sshd` is running and the public key is present, but OpenSSH refuses the authorized_keys file because its permissions are too open. Authentication fails even though the key material matches. Inspect ownership and mode bits on `~/.ssh` and `authorized_keys`, tighten them to what OpenSSH accepts, and retry the login. This station is about SSH’s strict file permission rules, not about generating new keys.

## Scenario
sshd is running and the public key is present, but OpenSSH refuses the authorized_keys file because its permissions are too open. Authentication fails even though the key material matches.

Inspect ownership and mode bits on ~/.ssh and authorized_keys, tighten them to what OpenSSH accepts, and retry the login. This station is about SSH’s strict file permission rules, not about generating new keys.

private key

authorized_keys mode

login

Click to expand

## Objective
SSH login as ctf succeeds after permissions are corrected.

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
