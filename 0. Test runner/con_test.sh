#!/bin/env bash
set -euo pipefail

solution=solution.py
timeoutvalue=15s
if [ $# == 1 ] ; then
    solution=$1
fi
i=0
filenames="input*.txt"
for filename in $filenames
do
    i=$((i+1))
    cp $filename input.txt
    timeout $timeoutvalue python3 $solution < input.txt > res$i.txt && ( diff --color=always --unified res$i.txt output$i.txt && echo -e "TEST $i \033[32mOK\033[39m" || echo -e "TEST $i \033[31mFailed\033[39m"  ) || echo "TEST $i \033[33mTimeout\033[39m ($timeoutvalue)"
    rm input.txt res$i.txt
done
