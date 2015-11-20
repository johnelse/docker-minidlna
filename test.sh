#!/bin/sh

set -eux

make

mkdir -p /tmp/media

CONTAINER=`./run.py \
    --name travis \
    --inotify \
    /tmp/media`

sleep 5

wget 127.0.0.1:8200

docker stop $CONTAINER
docker rm $CONTAINER
