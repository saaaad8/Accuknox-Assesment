#!/bin/bash

APP_URL="http://0.0.0.0:4499"
TIMEOUT=5

STATUS_CODE=$(curl -s -o /dev/null -w "%{http_code}" --max-time $TIMEOUT $APP_URL)

if [ "$STATUS_CODE" -eq 200 ]; then
    echo "$(date): Application is UP (Status $STATUS_CODE)"
else
    echo "$(date): Application is DOWN (Status $STATUS_CODE)"
fi
