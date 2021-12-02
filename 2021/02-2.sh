let x=0
let d=0
let a=0

while read -a line; do
    cmd=${line[0]}
    dist=${line[1]}

    case $cmd in
        forward)
            let x=x+$dist
            let d=d+a*$dist
            ;;
        down) let a=a+$dist ;;
        up) let a=a-$dist ;;
    esac
done

echo $(( x*d ))
