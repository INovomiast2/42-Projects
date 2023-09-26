#!/bin/bash

if [ $# -eq 0 ]; then
    echo "NO NAMES WHERE PASSED!";
    exit 1;
fi

for arg in "$@"; do
    dirname="ex-${arg}";

    mkdir "$dirname";
done