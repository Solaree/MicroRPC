#!/bin/bash

trap 'killall python3' EXIT
/usr/bin/micro "$@" </dev/null >/dev/null 2>&1 &

MICRO_PID=$!
sleep 0.5

python3 $HOME/.config/micro/plug/MicroRPC/rpc.py "$@" &
wait $MICRO_PID
