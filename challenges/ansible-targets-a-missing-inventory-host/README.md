# Ansible targets a missing inventory host

| Field | Value |
|-------|-------|
| **Level** | Beginner |
| **Kind** | Terminal |
| **Topics** | Ansible, Linux |
| **Checker** | ON / OFF (toggle di WebGUI) |
| **Base Points** | 10 |

## Description
An Ansible playbook is supposed to write a healthy marker on localhost, but the play targets a host name that is missing from the inventory. The play runs against an empty host set and leaves the marker unchanged. Fix the inventory or the play hosts pattern so localhost is selected, re-run the playbook, and confirm the marker file exists with the expected content.

## Scenario
An Ansible playbook is supposed to write a healthy marker on localhost, but the play targets a host name that is missing from the inventory. The play runs against an empty host set and leaves the marker unchanged.

Fix the inventory or the play hosts pattern so localhost is selected, re-run the playbook, and confirm the marker file exists with the expected content.

playbook

inventory

localhost file

Click to expand

## Objective
/opt/app/ansible.ok contains READY after the playbook runs.

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
- Base points: 10
- Mode checker ON: full points. OFF: 0.5×.
- Bonus: tanpa paste + WPM tinggi.
