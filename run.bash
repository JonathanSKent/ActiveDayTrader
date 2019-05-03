#!/bin/bash
difference=$(($(date -d "8:29" +%s) - $(date +%s)))

echo Waiting $difference

if [ $difference -lt 0 ]
then
    sleep $((86400 + difference))
else
    sleep $difference
fi

echo 'Beginning program'

python3.6 '/home/jonathan/Desktop/ActiveDayTrader/Main.py'
