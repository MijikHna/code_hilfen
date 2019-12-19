#!/usr/bin/env bash
sleep 5

if [ ! -d /app/code/nestjslernen/ ]
then
    echo "NEST.js Project existiert noch nicht"
    cd /app/code/
    nest new nestjslernen
    cd /app/code/nestjslernen/
    npm install
fi
echo "alles jut: NEST.js Project wird gestartet"
cd /app/code/nestjslernen/
echo "Exec macht: $@"
exec "$@"