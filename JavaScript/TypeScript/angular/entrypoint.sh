#!/usr/bin/env bash
sleep 5

# Angualar
if [ ! -d /srv/angular ]
then
    echo "Angular Project existiert noch nicht"
    cd /srv
    ng new  angular --defaults=true --skip-git --package-manager npm
    #cp /scripts/nodemon-debug.json /app/code/${ANGULARORDNER}/nodemon-debug.json
fi


cd /srv/angular
npm install

cd /srv/angular
#ng serve --open --port 4200 --host "0.0.0.0" #--port 8000
echo "EXEC: $@"
exec "$@"