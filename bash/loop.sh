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