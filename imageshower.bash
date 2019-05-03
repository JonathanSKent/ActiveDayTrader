#!/bin/bash
while [ $(date +'%H') -lt 15 ]
do
	timeout 10 feh -x --geometry +1000+500 '/home/jonathan/holdings.png' & timeout 10 feh -x --geometry +1000+0 '/home/jonathan/assets.png'
done
