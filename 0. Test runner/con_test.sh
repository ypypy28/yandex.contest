#!/bin/env bash
set -euo pipefail

solution=solution.py
timeoutvalue=15
onlytest=0

usage () {
    script_name=$(basename $0)
    cat << EOUSAGE
${script_name^^} - test runner of your python solutions of the Yandex Contest tasks

Usage:  ${script_name} [ -h ] [ -t NUM ] [ -n NUM ] [ SCRIPT_NAME ]

Where:
    -h              show this help message and exit
    -t NUM          set the timeout value in seconds (default: $timeoutvalue)
    -n NUM          run only NUM test, if 0 runs all the tests (default: 0)
    SCRIPT_NAME     name of the file with your solution (default: $solution)

pkg home page: https://github.com/ypypy28/yandex.contest
EOUSAGE
}

seconds_since() {
    printf $(( `date +%s` - $1 )) 
}

while getopts ":hn:t:" Option
do
    case $Option in
        h) usage ; exit 0 ;;
        t) timeoutvalue=$OPTARG ;;
        n) onlytest=$OPTARG ;;
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
if [ ! $onlytest -eq 0 ] ; then
    i=$(( $onlytest - 1 ))
    filenames="input${onlytest}.txt"
fi

for filename in $filenames
do
    i=$((i+1))
    cp input${i}.txt input.txt
    start_time=$(date +%s)
    timeout ${timeoutvalue}s python3 $solution < input.txt > res$i.txt && ( diff --color=always --unified res$i.txt output${i}.txt && echo -en "TEST $i \033[32mOK\033[39m" || echo -en "TEST $i \033[31mFailed\033[39m"  ) || echo -en "TEST $i \033[33mTimeout\033[39m (${timeoutvalue}s)"
    echo " (took $(seconds_since $start_time) seconds)"
    rm input.txt res$i.txt
done
