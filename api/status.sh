#!/usr/bin/env bash

if [ -f "./pid/rest.pid" ]; then
    REST_PID=`cat ./pid/rest.pid`
    echo "REST server is RUNNING at PID: ${REST_PID}"
else
    echo "REST server NOT RUNNING"
fi