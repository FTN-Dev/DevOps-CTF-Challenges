FROM redis:7
RUN apt-get update && apt-get install -y --no-install-recommends \
    curl procps iproute2 dnsutils python3 bash 2>/dev/null; rm -rf /var/lib/apt/lists/* 2>/dev/null || true
COPY config/ /opt/challenge-config/
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh
EXPOSE 6379
ENTRYPOINT ["/entrypoint.sh"]