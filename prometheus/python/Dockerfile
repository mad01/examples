FROM python:3.5-alpine

# adding code
WORKDIR /app/prom-exporter
ADD requirements.txt /app/prom-exporter

# install
RUN apk add --update openssl bash \
    && apk --update add --no-cache --virtual build-dependencies libc-dev autoconf gcc \
    && pip install --no-cache-dir -r requirements.txt \
    \ 
    && rm -rf ~/.cache \
    && apk del build-dependencies

ADD . /app/prom-exporter

EXPOSE 9999
ENTRYPOINT gunicorn --bind 0.0.0.0:9999 prom_exporter.app:api
