#!/bin/env bash
set -euo pipefail
i=0
filenames=./input*.txt
for filename in $filenames
do
    i=$((i+1))
    cat input$i.txt | python3 solution.py > res$i.txt
    diff --color=always --unified res$i.txt output$i.txt && echo "TEST $i OK"
done
rm res*.txt
