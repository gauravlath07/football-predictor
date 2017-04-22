#!/usr/bin/env bash
OLD_DIR=`pwd`
cd "${0%/*}"
sh ./stop.sh
sh ./start.sh
cd ${OLD_DIR}