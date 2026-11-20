#!/bin/bash
# Create directories
mkdir -p /opt/backup/output /opt/backup/logs /opt/backup/data
# Copy broken config
cp -r /opt/challenge-config/* /opt/backup/ 2>/dev/null
# Create backup data
echo "sample data" > /opt/backup/data/sample.txt
# Install cron file WITHOUT trailing newline (broken state)
printf '2 * * * * root /opt/backup/backup.sh\n' > /etc/cron.d/backup-job
# Remove trailing newline to create broken state
python3 -c "
data = open('/etc/cron.d/backup-job','rb').read()
if data.endswith(b'\n'):
    data = data[:-1]
open('/etc/cron.d/backup-job','wb').write(data)
"
# Ensure permissions
chmod 644 /etc/cron.d/backup-job
chmod +x /opt/backup/backup.sh
# Start cron daemon
service cron start
# Keep container alive
exec /bin/bash -c "tail -f /dev/null"