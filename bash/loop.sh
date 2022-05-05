#!/bin/bash

# Simple form of a for loop

for f in `cat README.txt`
do
    echo $f
done

# simple form of a while

while read line
do 
    echo $line
done < README.txt

# infinite loop
while 1 :
do
    echo $SECONDS
done

# timed loop
# +1 will define how many time the loop will last
end=$((SECONDS+1))
while [ $SECONDS -lt $end ]; do
    echo $SECONDS
done
