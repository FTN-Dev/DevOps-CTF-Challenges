FROM hashicorp/terraform:latest
COPY config/ /opt/challenge-config/
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh 2>/dev/null || true
ENTRYPOINT ["/entrypoint.sh"]
