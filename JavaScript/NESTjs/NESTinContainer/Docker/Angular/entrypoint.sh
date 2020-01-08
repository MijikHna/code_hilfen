#!/usr/bin/env bash
sleep 5

ANGULARORDNER=angularlernen

# Angualar
if [ ! -d /app/${ANGULARORDNER}/ ]
then
    echo "Angular Project existiert noch nicht"
    cd /app
    #(echo 'y'; sleep 5; echo '/n') | ng new ${ANGULARORDNER}
    ng new ${ANGULARORDNER} --defaults=true
    cd /app/${ANGULARORDNER}
    #npm install
    npm install jquery --save-dev
    npm install bootstrap --save-dev
    
    #cp /scripts/nodemon-debug.json /app/code/${ANGULARORDNER}/nodemon-debug.json
fi

#Lock-Dateien konvertieren
synp --source-file /app/${ANGULARORDNER}/package-lock.json

cd /app/${ANGULARORDNER}
ng serve --open --port 4200 --host "0.0.0.0"
#--port 8000
#echo "alles jut: ANGULAR Project wird gestartet"
#echo "Exec macht: $@"
#exec "$@"