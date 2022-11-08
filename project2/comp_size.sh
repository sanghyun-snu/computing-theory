#!/bin/bash


I=`wc -c $1 | cut -d' ' -f1`
J=`wc -c $2 | cut -d' ' -f1`
if [ $I -eq $J ]
then
      echo $1 $2 >> $1.pares
fi
