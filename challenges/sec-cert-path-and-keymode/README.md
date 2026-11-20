# Sec Cert Path And Keymode

| Field | Value |
|-------|-------|
| **Level** | Intermediate |
| **Kind** | Terminal |
| **Topics** | Security Hardening, Linux |
| **Checker** | ON / OFF (toggle di WebGUI) |
| **Base Points** | 25 |

## Description
The TLS cert path is wrong and the private key mode is too open.

## Scenario
The TLS cert path is wrong and the private key mode is too open.

cause A

cause B

healthy

Click to expand

## Objective
HTTPS probe on :8443 returns OK.

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
- Base points: 25
- Mode checker ON: full points. OFF: 0.5×.
- Bonus: tanpa paste + WPM tinggi.
