#!/bin/bash
echo "Start Get Data from https://www.ventusky.com"

lon=0
while(( $lon<360 ))
do
    lat=-90
    while(( $lat<90 ))
    do
        echo $lat
        let lat+=18
        nohup bash getdata.sh $lon $lat &
    done
    let lon++
done