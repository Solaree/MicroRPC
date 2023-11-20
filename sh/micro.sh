#!/bin/bash

function on_micro_exit() {
   killall python3
}

trap 'on_micro_exit "$@"' EXIT
micro "$@" </dev/null >/dev/null 2>&1 &

MICRO_PID=$!
sleep 0.5

python3 ~/.config/micro/plug/MicroRPC/rpc/rpc.pyz "$@" &
wait $MICRO_PID
