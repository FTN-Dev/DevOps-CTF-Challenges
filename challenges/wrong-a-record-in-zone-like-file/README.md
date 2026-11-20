# Wrong A record in zone-like file

| Field | Value |
|-------|-------|
| **Level** | Beginner |
| **Kind** | Terminal |
| **Topics** | DNS, Linux, Network Troubleshooting |
| **Checker** | ON / OFF (toggle di WebGUI) |
| **Base Points** | 10 |

## Description
Local resolver file maps app.local to 127.0.0.2.

## Scenario
Local resolver file maps app.local to 127.0.0.2.

## Objective
Restore the expected healthy behaviour. Symptom: Local resolver file maps app.local to 127.0.0.2.

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
