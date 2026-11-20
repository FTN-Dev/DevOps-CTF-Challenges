# DNS resolver pointed at a blackhole

| Field | Value |
|-------|-------|
| **Level** | Beginner |
| **Kind** | Terminal |
| **Topics** | DNS, Linux, Network Troubleshooting |
| **Checker** | ON / OFF (toggle di WebGUI) |
| **Base Points** | 10 |

## Description
Direct IP access works, but `api.internal` fails to resolve.

## Scenario
Direct IP access works, but api.internal fails to resolve.

## Objective
Restore the expected healthy behaviour. Symptom: Direct IP access works, but api.internal fails to resolve.

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
