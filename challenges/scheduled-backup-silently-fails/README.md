# Scheduled Backup Silently Fails

| Field | Value |
|-------|-------|
| **Level** | Beginner |
| **Topics** | Linux, Bash Scripting |
| **Base Points** | 10 |

## Description

A daily backup cron job at `/opt/backup/backup.sh` should run every night at 2 AM
and produce archive files in `/opt/backup/output/`. No new backup files have appeared
for 3 days. The service appears healthy but the scheduled task never fires.

## Objective

Fix the cron configuration so the backup job runs successfully and produces new
archive files in `/opt/backup/output/`.

## Hint

Check the cron file with `cat -A`. Is there something missing at the end of the file?

## How to solve (PoC)

1. Inspect: `cat /etc/cron.d/backup-job` → looks correct at first glance
2. Investigate: `cat -A /etc/cron.d/backup-job` → notice missing trailing newline
3. Fix: add a trailing newline to the cron file
4. Verify: wait for cron to trigger, or run `/opt/backup/backup.sh` manually
5. Confirm: `ls /opt/backup/output/` shows new archive files

## Scoring

- Base points: 10
- Mode checker ON: full points. OFF: 0.5×.
- Bonus: without paste + high WPM.
