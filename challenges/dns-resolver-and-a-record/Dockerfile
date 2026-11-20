FROM ubuntu:22.04
ENV DEBIAN_FRONTEND=noninteractive
RUN apt-get update && apt-get install -y --no-install-recommends \
    dnsmasq bind9utils curl procps && rm -rf /var/lib/apt/lists/*
COPY config/ /opt/challenge-config/
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh
EXPOSE 53
ENTRYPOINT ["/entrypoint.sh"]
