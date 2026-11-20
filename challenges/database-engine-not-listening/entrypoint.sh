#!/bin/bash
# Initialize data directory if needed
if [ ! -f /var/lib/postgresql/data/PG_VERSION ]; then
    mkdir -p /var/lib/postgresql/data
    chown postgres:postgres /var/lib/postgresql/data
    su postgres -c "initdb -D /var/lib/postgresql/data" >/dev/null 2>&1
fi
# Do NOT start PostgreSQL (broken state: service down)
# Keep container alive
exec /bin/bash -c "tail -f /dev/null"