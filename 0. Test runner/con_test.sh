#!/bin/env bash
set -euo pipefail

seconds_since() {
    printf $(( `date +%s` - $1 )) 
}

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
    start_time=$(date +%s)
    timeout $timeoutvalue python3 $solution < input.txt > res$i.txt && ( diff --color=always --unified res$i.txt output$i.txt && echo -en "TEST $i \033[32mOK\033[39m" || echo -en "TEST $i \033[31mFailed\033[39m"  ) || echo -en "TEST $i \033[33mTimeout\033[39m ($timeoutvalue)"
    echo " (took $(seconds_since $start_time) seconds)"
    rm input.txt res$i.txt
done
