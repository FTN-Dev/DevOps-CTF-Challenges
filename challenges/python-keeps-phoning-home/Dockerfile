FROM ubuntu:22.04
ENV DEBIAN_FRONTEND=noninteractive
RUN apt-get update && apt-get install -y --no-install-recommends \
    python3 python3-pip curl procps net-tools && rm -rf /var/lib/apt/lists/*

COPY config/ /opt/challenge-config/

COPY config/setup.sh /setup.sh
RUN chmod +x /setup.sh && /setup.sh

RUN mkdir -p /opt/billing-api /opt/collector
COPY config/helper.py /opt/billing-api/helper.py
COPY config/billing_api.py /opt/billing-api/billing_api.py
COPY config/collector.py /opt/collector/collector.py
COPY config/sitecustomize.py /usr/lib/python3/dist-packages/sitecustomize.py

COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]