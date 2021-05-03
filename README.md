# About
This is based on the TICK stack:
https://www.influxdata.com/blog/introduction-to-influxdatas-influxdb-and-tick-stack/

Telegraf is the collector.
Influxdb is the DB.
grafana displays the data.

The idea is to provide a open source tool to use for lab testing telemetry.

# How to contribute
https://www.dataschool.io/how-to-contribute-on-github/

# Quick start
1. Edit the telegraf ./config/openconfig.conf file.
  - Add hosts.
  - Adjust sensor pull timers as needed.
2. cd influx; ./run_influxdb 
3. cd telegraf; ./run_telegraf
4. cd grafana; ./run_grafana
5. open htttp://<your host>:3300





