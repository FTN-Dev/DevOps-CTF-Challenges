#!/bin/bash
# Copy config
cp /opt/challenge-config/redis.conf /opt/redis/redis.conf 2>/dev/null
mkdir -p /opt/redis
cp /opt/challenge-config/redis.conf /opt/redis/redis.conf 2>/dev/null
# Do NOT start Redis (broken state: service down)
# Keep container alive
exec /bin/bash -c "tail -f /dev/null"