# Blackhole nameserver listed first

| Field | Value |
|-------|-------|
| **Level** | Beginner |
| **Kind** | Terminal |
| **Topics** | DNS, Linux, Network Troubleshooting |
| **Checker** | ON / OFF (toggle di WebGUI) |
| **Base Points** | 10 |

## Description
resolv.conf lists a blackhole DNS first; lookups hang/fail.

## Scenario
resolv.conf lists a blackhole DNS first; lookups hang/fail.

## Objective
Restore the expected healthy behaviour. Symptom: resolv.conf lists a blackhole DNS first; lookups hang/fail.

## Hint
Cek A record / resolver / hosts. Bandingkan dengan IP yang diharapkan.

## Allowed to change
_TODO: daftar file/config yang boleh diubah._

## Must NOT change
_TODO: daftar file/config yang dilarang diubah._

## How to solve (PoC)
<details>
<summary>Show solution</summary>

DNS

</details>

## Scoring
- Base points: 10
- Mode checker ON: full points. OFF: 0.5×.
- Bonus: tanpa paste + WPM tinggi.
