#!/usr/bin/env bash
set -e
docker run --net=host \
 -v $PWD:/etc/prometheus \
 prom/alertmanager \
 -config.file=/etc/prometheus/alertmanager.yml   

