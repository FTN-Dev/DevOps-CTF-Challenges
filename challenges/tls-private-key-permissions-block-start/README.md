# TLS private key permissions block start

| Field | Value |
|-------|-------|
| **Level** | Beginner |
| **Kind** | Terminal |
| **Topics** | Security Hardening, Linux |
| **Checker** | ON / OFF (toggle di WebGUI) |
| **Base Points** | 10 |

## Description
A tiny TLS server refuses to start because the private key file mode is too open. The certificate and key paths are otherwise correct. Tighten the private key permissions, start the TLS listener on the documented port, and confirm an HTTPS probe succeeds.

## Scenario
A tiny TLS server refuses to start because the private key file mode is too open. The certificate and key paths are otherwise correct.

Tighten the private key permissions, start the TLS listener on the documented port, and confirm an HTTPS probe succeeds.

key mode

TLS server

HTTPS probe

Click to expand

## Objective
HTTPS probe to 127.0.0.1:8443 returns OK.

## Hint
Cek cert path, key mode, permission file.

## Allowed to change
_TODO: daftar file/config yang boleh diubah._

## Must NOT change
_TODO: daftar file/config yang dilarang diubah._

## How to solve (PoC)
<details>
<summary>Show solution</summary>

1. Inspect: cek cert path, key mode, permission.
2. Perbaiki path / mode / ownership sesuai objective.
3. Reload service.
4. Verifikasi: service sehat, cert valid.
5. Verify: klik "Verify" di WebGUI → checker PASS.

</details>

## Scoring
- Base points: 10
- Mode checker ON: full points. OFF: 0.5×.
- Bonus: tanpa paste + WPM tinggi.
