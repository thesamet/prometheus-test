#!/usr/bin/env bash
set -e
docker run --net=host -i -p 3000:3000 grafana/grafana
