FROM ubuntu:22.04
ENV DEBIAN_FRONTEND=noninteractive
RUN apt-get update && apt-get install -y --no-install-recommends \
    dnsutils dnsmasq curl procps iproute2 bash net-tools && rm -rf /var/lib/apt/lists/*

COPY config/ /opt/challenge-config/
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

EXPOSE 80 53
ENTRYPOINT ["/entrypoint.sh"]