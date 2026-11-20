#!/bin/bash
# Copy broken nginx config
cp /opt/challenge-config/nginx.conf /etc/nginx/sites-enabled/default
# Start app on 8080
python3 /opt/challenge-config/app.py >/tmp/app.log 2>&1 &
# Start nginx
nginx
# Keep alive
exec /bin/bash -c "tail -f /dev/null"