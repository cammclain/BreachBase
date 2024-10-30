#!/bin/bash
while true; do
  TASK=$(mosquitto_sub -h mqtt_broker -t "tasks" -C 1)
  if [ "$TASK" ]; then
    echo "Received task: $TASK"
    bbot $TASK --output /output/result.json
    mosquitto_pub -h mqtt_broker -t "results" -f /output/result.json
  fi
  sleep 5
done
