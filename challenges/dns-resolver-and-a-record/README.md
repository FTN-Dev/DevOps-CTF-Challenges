# DNS resolver and A record

| Field | Value |
|-------|-------|
| **Level** | Intermediate |
| **Kind** | Terminal |
| **Topics** | DNS, Linux |
| **Checker** | ON / OFF (toggle di WebGUI) |
| **Base Points** | 25 |

## Description
The app resolver points at the wrong address and the DNS sidecar serves the wrong A record.

## Scenario
The app resolver points at the wrong address and the DNS sidecar serves the wrong A record.

workspace

dns

healthy

Click to expand

## Objective
App resolves app.internal to the healthy address.

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
- Base points: 25
- Mode checker ON: full points. OFF: 0.5×.
- Bonus: tanpa paste + WPM tinggi.
