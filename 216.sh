#!/usr/bin/env zsh

# set -x
# 
# ./216 "$1" > x

while read -n x; do                            
    factor $x &
done < x > factored

egrep '^([0-9]+): \1' factored | wc -l
