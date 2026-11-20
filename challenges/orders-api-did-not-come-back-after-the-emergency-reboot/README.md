# orders-api did not come back after the emergency reboot

| Field | Value |
|-------|-------|
| **Level** | Intermediate |
| **Kind** | Terminal |
| **Topics** | Linux, Bash Scripting, Systemd |
| **Checker** | ON / OFF (toggle di WebGUI) |
| **Base Points** | 25 |

## Description
Last week a critical kernel patch (tracked publicly as PwnEscape / CVE-2026-99999) forced rolling host reboots across several providers, including a Fly.io incident on 16 Oct 2026. This host was among them. orders-api is a small internal HTTP service that talks to an inventory dependency on the same machine. Before the reboot an on-call engineer could start it by hand and `/health` returned 200. After the host came back up, the process supervisor is running, but orders-api is not answering on its configured port and `/health` fails. Bring orders-api back under the process supervisor so that a fresh boot leaves it healthy. Keep the application binary, its config file under `/etc/orders/`, and the listening port exactly as they are. Do not replace the supervisor with a one-shot background process.

## Scenario
Last week a critical kernel patch (tracked publicly as PwnEscape / CVE-2026-99999) forced rolling host reboots across several providers, including a Fly.io incident on 16 Oct 2026. This host was among them.

orders-api is a small internal HTTP service that talks to an inventory dependency on the same machine. Before the reboot an on-call engineer could start it by hand and /health returned 200. After the host came back up, the process supervisor is running, but orders-api is not answering on its configured port and /health fails.

Bring orders-api back under the process supervisor so that a fresh boot leaves it healthy. Keep the application binary, its config file under /etc/orders/, and the listening port exactly as they are. Do not replace the supervisor with a one-shot background process.

## Objective
Make orders-api start automatically under supervisord after boot, with the environment it needs, so /health returns 200 and the inventory dependency is reached.

## Hint
Cek service/process/config yang relevan. Identifikasi misconfig.

## Allowed to change
_TODO: daftar file/config yang boleh diubah._

## Must NOT change
_TODO: daftar file/config yang dilarang diubah._

## How to solve (PoC)
<details>
<summary>Show solution</summary>

1. Inspect: cek service/process/config yang relevan.
2. Identifikasi misconfig (port, permission, path, user).
3. Perbaiki sesuai objective.
4. Restart service jika perlu.
5. Verifikasi: health check / command test.
6. Verify: klik "Verify" di WebGUI → checker PASS.

</details>

## Scoring
- Base points: 25
- Mode checker ON: full points. OFF: 0.5×.
- Bonus: tanpa paste + WPM tinggi.
