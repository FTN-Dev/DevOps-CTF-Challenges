#!/bin/bash
# Copy broken nginx config
cp /opt/challenge-config/default /etc/nginx/sites-enabled/default 2>/dev/null
# Ensure web root has content
mkdir -p /var/www/html
echo '<h1>OK</h1>' > /var/www/html/index.html
# Ensure nginx pid directory exists
mkdir -p /run/nginx
# Start nginx (will fail due to syntax error in broken config)
nginx 2>/tmp/nginx_error.log
# Keep container alive
exec /bin/bash -c "tail -f /dev/null"