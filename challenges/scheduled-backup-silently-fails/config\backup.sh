#!/bin/bash
# Daily backup script
DATE=$(date +%Y%m%d_%H%M%S)
tar -czf /opt/backup/output/backup_${DATE}.tar.gz /opt/backup/data/ 2>/dev/null
echo "Backup completed: backup_${DATE}.tar.gz" >> /opt/backup/logs/backup.log