#!/usr/bin/env bash
set -e
docker run --net=host \
 -v $PWD:/etc/prometheus \
 prom/prometheus -alertmanager.url=http://localhost:9093 \
 -config.file=/etc/prometheus/prometheus.yml   

