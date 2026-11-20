# Ansible when condition never fires

| Field | Value |
|-------|-------|
| **Level** | Beginner |
| **Kind** | Terminal |
| **Topics** | Ansible, Linux |
| **Checker** | ON / OFF (toggle di WebGUI) |
| **Base Points** | 10 |

## Description
The only task that writes the healthy marker is gated by a `when` condition that is always false. The playbook “succeeds” but never creates the file the checker expects. Adjust the condition (or remove it) so the copy task runs, re-run the playbook, and verify the marker.

## Scenario
The only task that writes the healthy marker is gated by a when condition that is always false. The playbook “succeeds” but never creates the file the checker expects.

Adjust the condition (or remove it) so the copy task runs, re-run the playbook, and verify the marker.

skipped

fixed

copy task

when: false

marker

Click to expand

## Objective
Playbook writes /opt/app/ansible.ok with READY.

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
