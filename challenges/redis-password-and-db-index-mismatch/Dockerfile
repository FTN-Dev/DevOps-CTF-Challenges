FROM redis:7
COPY config/redis.conf /usr/local/etc/redis/redis.conf 2>/dev/null || true
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh 2>/dev/null || true
EXPOSE 6379
ENTRYPOINT ["/entrypoint.sh"]
