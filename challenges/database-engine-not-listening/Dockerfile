FROM postgres:15
ENV POSTGRES_PASSWORD=postgres
RUN apt-get update && apt-get install -y --no-install-recommends \
    curl procps iproute2 dnsutils python3 bash && rm -rf /var/lib/apt/lists/* 2>/dev/null || true
COPY config/ /opt/challenge-config/
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh
EXPOSE 5432
ENTRYPOINT ["/entrypoint.sh"]