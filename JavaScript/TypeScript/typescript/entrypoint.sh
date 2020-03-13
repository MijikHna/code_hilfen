#!/usr/bin/env bash
sleep 5

declare -a EXEC_ARRAY

# create folder
echo "/srv/$1"
if [ ! -d /srv/$1 ]
then
    echo "NO TS Project installed"
    mkdir -p /srv/$1
    cd /srv/$1
    npm init -y
    tsc --init
    #npm install commonjs systemjs @types/node rxjs
fi

cd /srv/$1
ls -l
npm install

# shift parameters
#echo "Lenght ARRAY: $#"
ARGS=("$@")
echo "ARGS: ${ARGS[*]}"
for (( i=1; i<${#ARGS[*]}; i++ ))
do
    EXEC_ARRAY[$i-1]=${ARGS[$i]}
done

cd /srv/$1
echo "EXEC: ${EXEC_ARRAY[*]}"
exec ${EXEC_ARRAY[*]}