# syntax=docker/dockerfile:1

FROM mariadb:latest

ENV MARIADB_USER mitmirrordb
ENV MARIADB_PASSWORD fischer
ENV MARIADB_ROOT_PASSWORD fischer

COPY schema.sql /docker-entrypoint-initdb.d

EXPOSE 3306
