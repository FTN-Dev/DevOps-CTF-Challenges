# Ansible Inventory And Dest

| Field | Value |
|-------|-------|
| **Level** | Intermediate |
| **Kind** | Terminal |
| **Topics** | Ansible, Linux |
| **Checker** | ON / OFF (toggle di WebGUI) |
| **Base Points** | 25 |

## Description
The play targets a missing inventory host and the copy dest path is wrong.

## Scenario
The play targets a missing inventory host and the copy dest path is wrong.

cause A

cause B

healthy

Click to expand

## Objective
/opt/app/ansible.ok contains READY.

## Hint
Cek konfigurasi yang relevan dengan objective. Identifikasi apa yang salah.

## Allowed to change
_TODO: daftar file/config yang boleh diubah._

## Must NOT change
_TODO: daftar file/config yang dilarang diubah._

## How to solve (PoC)
<details>
<summary>Show solution</summary>

1. Inspect: `ansible-playbook --check playbook.yml`.
2. Cek when condition / handler / inventory.
3. Perbaiki sesuai objective.
4. Run: `ansible-playbook playbook.yml`.
5. Verifikasi: output OK, handler triggered.
6. Verify: klik "Verify" di WebGUI → checker PASS.

</details>

## Scoring
- Base points: 25
- Mode checker ON: full points. OFF: 0.5×.
- Bonus: tanpa paste + WPM tinggi.
