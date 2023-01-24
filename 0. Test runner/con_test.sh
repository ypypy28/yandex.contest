#!/bin/env bash
set -euo pipefail

solution=solution.py
timeoutvalue=15

usage () {
    script_name=$(basename $0)
    cat << EOUSAGE
${script_name^^} - test runner of your python solutions of the Yandex Contest tasks

Usage:  ${script_name} [ -h ] [ -t NUM ] [ SCRIPT_NAME ]

Where:
    -h              show this help message and exit
    -t NUM          set the timeout value in seconds (default: $timeoutvalue)
    SCRIPT_NAME     name of the file with your solution (default: $solution)

pkg home page: https://github.com/ypypy28/yandex.contest
EOUSAGE
}

seconds_since() {
    printf $(( `date +%s` - $1 )) 
}

while getopts ":hf:t:" Option
do
    case $Option in
        h) usage ; exit 0 ;;
        t) timeoutvalue=$OPTARG ;;
        \?) echo BAD OPTION: ${@: $(( $OPTIND-1 ))} >&2 ; usage ; exit 1 ;;
    esac
done

if [ $# -eq $OPTIND ] ; then
    solution=${@: -1}
fi

if [ ! -f "$solution" ] ; then
   echo "python script \"$solution\" does not exist" >&2
   exit 1
fi

i=0
filenames="input*.txt"
for filename in $filenames
do
    i=$((i+1))
    cp $filename input.txt
    start_time=$(date +%s)
    timeout ${timeoutvalue}s python3 $solution < input.txt > res$i.txt && ( diff --color=always --unified res$i.txt output$i.txt && echo -en "TEST $i \033[32mOK\033[39m" || echo -en "TEST $i \033[31mFailed\033[39m"  ) || echo -en "TEST $i \033[33mTimeout\033[39m (${timeoutvalue}s)"
    echo " (took $(seconds_since $start_time) seconds)"
    rm input.txt res$i.txt
done
