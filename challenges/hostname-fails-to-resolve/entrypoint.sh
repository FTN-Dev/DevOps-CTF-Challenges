#!/bin/bash
# Copy broken resolv.conf (wrong nameserver)
cp /opt/challenge-config/resolv.conf /etc/resolv.conf
# Create dnsmasq config that resolves api.internal to 127.0.0.1
mkdir -p /etc/dnsmasq.d
echo "address=/api.internal/127.0.0.1" > /etc/dnsmasq.d/api.conf
echo "listen-address=127.0.0.1" >> /etc/dnsmasq.d/api.conf
echo "port=53" >> /etc/dnsmasq.d/api.conf
# Start dnsmasq on 127.0.0.1:53
dnsmasq -C /etc/dnsmasq.d/api.conf 2>/tmp/dns.log || dnsmasq --listen-address=127.0.0.1 --port=53 --address=/api.internal/127.0.0.1 2>/tmp/dns.log
# Keep container alive
exec /bin/bash -c "tail -f /dev/null"