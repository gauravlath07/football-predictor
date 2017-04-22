#!/usr/bin/env bash
OLD_DIR=`pwd`
REST_PORT=9612

cd "${0%/*}"

if [ -f "./pid/rest.pid" ]; then
    REST_PID=`cat ./pid/rest.pid`
    echo "Stopping REST server at PID: ${REST_PID}"
    kill -9 ${REST_PID}
    rm "./pid/rest.pid"
else
    echo "REST server is not running!"
fi

echo "Searching for orphan processes on port: ${REST_PORT}"

for x in `lsof -i:${REST_PORT} | egrep ${REST_PORT} | tr -s ' ' | cut -d ' ' -f 2`; do
    echo "Stopping PID: ${x}";
    kill -9 ${x};
done

cd ${OLD_DIR}