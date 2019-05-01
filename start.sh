#!/usr/bin/env bash

echo "***************************** Step 1 ***************************************"

echo "Build new container"
docker build -t lesou:v1 .

echo "***************************** Step 2 ***************************************"
echo "Start new container"
docker run --restart="always" -d -p 9090:8099 \
    -e 'LANG=zh_CN.UTF-8' \
    -e 'LANGUAGE=zh_CN.UTF-8' \
    -e 'LC_ALL=zh_CN.UTF-8' \
    --name lesou \
    lesou:v1
echo ""