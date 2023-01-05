#!/bin/env bash
set -euo pipefail

solution=solution.py
if [ $# == 1 ] ; then
    solution=$1
fi
i=0
filenames="input*.txt"
for filename in $filenames
do
    i=$((i+1))
    cp $filename input.txt
    cat input.txt | python3 $solution > res$i.txt
    diff --color=always --unified res$i.txt output$i.txt && echo "TEST $i OK" || echo "TEST $i Failed"
    rm input.txt res$i.txt
done
