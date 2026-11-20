FROM postgres:15
ENV POSTGRES_PASSWORD=postgres
COPY config/pg_hba.conf /etc/postgresql/pg_hba.conf 2>/dev/null || true
COPY config/postgresql.conf /etc/postgresql/postgresql.conf 2>/dev/null || true
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh 2>/dev/null || true
EXPOSE 5432
ENTRYPOINT ["/entrypoint.sh"]
