echo "Start Get Data from https://www.ventusky.com"

lon=0
while(( $lon<360 ))
do
    lat=-90
    while(( $lat<90 ))
    do
        nohup bash getdata.sh $lon $lat &
        let lat+=30
    done
    let lon+=30
done