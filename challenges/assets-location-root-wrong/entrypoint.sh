#!/bin/bash
# Copy broken config to target location
cp -r /opt/challenge-config/* /etc/ 2>/dev/null
cp -r /opt/challenge-config/* /opt/ 2>/dev/null
# Keep container alive for shell access
exec /bin/bash -c "tail -f /dev/null"
