#!/bin/bash
python3 /opt/collector/collector.py >/tmp/collector.log 2>&1 &
python3 /opt/billing-api/billing_api.py >/tmp/billing.log 2>&1 &
exec /bin/bash -c "tail -f /dev/null"