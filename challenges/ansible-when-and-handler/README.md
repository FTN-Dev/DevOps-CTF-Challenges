# Ansible When And Handler

| Field | Value |
|-------|-------|
| **Level** | Intermediate |
| **Kind** | Terminal |
| **Topics** | Ansible, Linux |
| **Checker** | ON / OFF (toggle di WebGUI) |
| **Base Points** | 25 |

## Description
A when:false skips the main task and a handler is never notified. Investigate both failure modes independently: correcting only one still leaves the checker red. Use the station files under `/opt` as the system of record, apply a minimal fix for each cause, then re-run the service or playbook the scenario depends on. Author notes (hidden from participants) encode the exact pair: when + notify.

## Scenario
A when:false skips the main task and a handler is never notified. Investigate both failure modes independently: correcting only one still leaves the checker red. Use the station files under /opt as the system of record, apply a minimal fix for each cause, then re-run the service or playbook the scenario depends on. Author notes (hidden from participants) encode the exact pair: when + notify.

cause A

cause B

healthy

Click to expand

## Objective
/opt/app/ansible.ok contains READY and /opt/app/handler.ok exists.

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
