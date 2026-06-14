#!/bin/bash

mkdir -p result

nsys profile --trace=osrt -o result/model_cpu python3 src/model_cpu.py
nsys stats --report osrt_sum result/model_cpu.nsys-rep > result/summary.txt
