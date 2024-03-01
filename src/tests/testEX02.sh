#!/bin/bash

answer=('True' 'False' 'False' 'Error' 'Error' 'False' 'False' 'False' 'Error' 'Error' 'Error' 'Error' 'Error' 'False' 'False' 'Error' 
        'False' 'False' 'Error' 'Error' 'Error' 'Error' 'False' 'Error' 'Error')

error=0
for (( i = 1; i <= 25; i++ ))
do
  result=$( echo 'tests/m'$i'.txt' | python3 mfinder.py )
  echo $i':' $result
  if [[ $result != ${answer[$i - 1]} ]]
  then
    error=1
  fi
done

if (( $error == 0 ))
then
  echo 'All tests is OK'
else
  echo 'Tests ERROR'
fi