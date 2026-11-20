# Python keeps phoning home

| Field | Value |
|-------|-------|
| **Level** | Intermediate |
| **Kind** | Terminal |
| **Topics** | Linux, Security Hardening, Bash Scripting |
| **Checker** | ON / OFF (toggle di WebGUI) |
| **Base Points** | 25 |

## Description
On 21 Oct 2026, LiteLLM 1.107.0 was reported compromised: a poisoned release dropped startup hooks that ran on every Python interpreter start and beaconed out to an attacker collector. This lab mirrors that class of incident on a small internal host. billing-api is still up and correctly imports its helper library, but something on this host keeps opening outbound HTTP connections to a collector listening on the same machine. Fresh `python3` processes appear to make it worse. Stop the outbound beacons permanently. Keep Python usable, keep billing-api healthy, and do not break the helper library import that billing-api depends on.

## Scenario
On 21 Oct 2026, LiteLLM 1.107.0 was reported compromised: a poisoned release dropped startup hooks that ran on every Python interpreter start and beaconed out to an attacker collector. This lab mirrors that class of incident on a small internal host.

billing-api is still up and correctly imports its helper library, but something on this host keeps opening outbound HTTP connections to a collector listening on the same machine. Fresh python3 processes appear to make it worse.

Stop the outbound beacons permanently. Keep Python usable, keep billing-api healthy, and do not break the helper library import that billing-api depends on.

## Objective
Eliminate the startup persistence and the running beacon process so new Python starts no longer contact the collector, while billing-api and its helper import keep working.

## Hint
Cek file startup Python (sitecustomize.py, .pth files di site-packages) dan proses yang berjalan. Ada sesuatu yang dieksekusi setiap kali Python start.

## Allowed to change
- `/usr/lib/python3/dist-packages/sitecustomize.py` — boleh dihapus
- `/usr/lib/python3/dist-packages/beacon.pth` — boleh dihapus

## Must NOT change
- `/opt/billing-api/billing_api.py`
- `/opt/billing-api/helper.py`

## How to solve (PoC)
<details>
<summary>Show solution</summary>

1. Inspect proses: `ps aux | grep collector` → temukan beacon process.
2. Kill process: `pkill -f collector.py`.
3. Cek startup hooks: `ls /usr/lib/python3/dist-packages/*.pth` dan `cat sitecustomize.py`.
4. Hapus persistence: `rm /usr/lib/python3/dist-packages/sitecustomize.py /usr/lib/python3/dist-packages/beacon.pth`.
5. Verifikasi: `python3 -c 'import site'` tidak ada beacon. `curl localhost:8080/health` → 200.
6. Verify: klik "Verify" di WebGUI → checker PASS.

</details>

## Scoring
- Base points: 25
- Mode checker ON: full points. OFF: 0.5×.
- Bonus: tanpa paste + WPM tinggi.