#!/bin/bash

mkdir -p result

/usr/lib/linux-tools-6.8.0-124/perf stat -I 10 -e cycles,instructions,cache-misses,page-faults python3 src/model.py 2>result/perf_stat.log
python3 tool/graph.py result/perf_stat.log
