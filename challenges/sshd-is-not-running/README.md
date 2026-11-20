# sshd is not running

| Field | Value |
|-------|-------|
| **Level** | Beginner |
| **Kind** | Terminal |
| **Topics** | Linux, Security Hardening |
| **Checker** | ON / OFF (toggle di WebGUI) |
| **Base Points** | 10 |

## Description
Operators expect to open an SSH session to the local host using the prepared key material. The SSH daemon is not running, so connections to the SSH port fail before authentication. Confirm `sshd` is absent, start it with the system host keys already present under `/etc/ssh`, and verify a successful key-based login to the challenge user. Keep the listener on the configured SSH port, not on the sandbox agent port.

## Scenario
Operators expect to open an SSH session to the local host using the prepared key material. The SSH daemon is not running, so connections to the SSH port fail before authentication.

Confirm sshd is absent, start it with the system host keys already present under /etc/ssh, and verify a successful key-based login to the challenge user. Keep the listener on the configured SSH port, not on the sandbox agent port.

ssh client

sshd

user shell

Click to expand

## Objective
Key-based SSH to ctf on port 2222 succeeds.

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
