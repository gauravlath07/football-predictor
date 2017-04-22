#!/bin/bash

OLD_DIR=`pwd`
cd "${0%/*}"

if [ ! -d "logs" ]; then
    mkdir "logs"
    chmod -R ug+rw "logs"
fi
if [ ! -d "pid" ]; then
    mkdir "pid"
    chmod -R ug+rw "pid"
fi

if [ ! -f "./pid/rest.pid" ]; then
    echo "Starting REST server"
    gunicorn -c rest_config.py rest_server:api
else
    REST_PID=`cat ./pid/rest.pid`
    echo "REST server is already running at PID: ${REST_PID}"
fi

echo "All services started. Use status.sh to check the status of the services."
cd ${OLD_DIR}