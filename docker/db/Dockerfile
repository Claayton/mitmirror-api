# syntax=docker/dockerfile:1

FROM mariadb:latest

COPY schema.sql /docker-entrypoint-initdb.d

EXPOSE 3306
