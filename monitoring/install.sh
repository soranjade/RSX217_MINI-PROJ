#! /bin/bash

mkdir -p  /opt/monitoring/etc/grafana/ /opt/monitoring/etc/prometheus/ /opt/monitoring/data/grafana/ /opt/monitoring/data/prometheus
chmod -R 777 /opt/monitoring/data

cp prometheus.yml /opt/monitoring/etc/prometheus/
