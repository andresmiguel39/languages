#!/bin/bash

# export variables in bash

export variable="Hello World"


echo $variable2
echo $variable 

echo "testing be `date` and $variable"

#check if variable is null
my_var="nixCraft"
if [ -z "$my_var" ]
then
      echo "\$my_var is NULL"
else
      echo "\$my_var is NOT NULL"
fi
