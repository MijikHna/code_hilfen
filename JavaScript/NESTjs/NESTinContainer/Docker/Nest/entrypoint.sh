#!/usr/bin/env bash
sleep 5

NESTJSORDNER=nestjslernen

# Nest.js
if [ ! -d /app/${NESTJSORDNER}/ ]
then
    echo "NEST.js Project existiert noch nicht"
    cd /app/
    echo '/n' | nest new ${NESTJSORDNER}
    cd /app/${NESTJSORDNER}/
    npm install
    
    #cp /scripts/nodemon-debug.json /app/code/${NESTJSORDNER}/nodemon-debug.json
fi

#Lock-Dateien konvertieren
synp --source-file /app/${NESTJSORDNER}/package-lock.json

cd /app/${NESTJSORDNER}
echo "alles jut: NESTJS Project wird gestartet"
echo "Exec macht: $@"
exec "$@"