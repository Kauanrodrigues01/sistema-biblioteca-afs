# Base build
FROM python:3.13.1-alpine3.21 AS base

ENV PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1

COPY requirements.txt .

RUN apk add --no-cache --virtual .build-deps \
    gcc linux-headers musl-dev \
    libffi-dev zlib-dev && \
    pip install --no-cache -r requirements.txt && \
    find /usr/local \
        \( -type d -a -name test -o -name tests \) \
        -o \( -type f -a -name '*.pyc' -o -name '*.pyo' \) \
        -exec rm -rf '{}' + && \
    runDeps="$( \
        scanelf --needed --nobanner --recursive /usr/local \
                | awk '{ gsub(/,/, "\nso:", $2); print "so:" $2 }' \
                | sort -u \
                | xargs -r apk info --installed \
                | sort -u \
    )" && \
    apk add --virtual .rundeps $runDeps && \
    apk del .build-deps


# Now multistage build
FROM python:3.13.1-alpine3.21

ENV PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1

COPY --from=base /usr/local/lib/python3.13/site-packages/ /usr/local/lib/python3.13/site-packages/
COPY --from=base /usr/local/bin/ /usr/local/bin/

RUN adduser -h /app -s /bin/bash -D userapp

WORKDIR /app

COPY . .

RUN find /usr/local \
    \( -type d -a -name test -o -name tests \) \
    -o \( -type f -a -name '*.pyc' -o -name '*.pyo' \) \
    -exec rm -rf '{}' + && \
    runDeps="$( \
    scanelf --needed --nobanner --recursive /usr/local \
            | awk '{ gsub(/,/, "\nso:", $2); print "so:" $2 }' \
            | sort -u \
            | xargs -r apk info --installed \
            | sort -u \
    )" && \
    apk add --virtual .rundeps $runDeps


RUN chown userapp:userapp /app && \
    mkdir -p /app/static && \
    chmod -R 777 /app/static && \
    mkdir -p /app/uwsgi && \
    chmod -R 777 /app/uwsgi

EXPOSE 80

USER userapp
