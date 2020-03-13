#!/usr/bin/env bash
sleep 5

cd /srv

# Nest.js
if [ ! -d /srv/nestjs ]
then
    echo "NEST.js Project existiert noch nicht"
    cd /srv
    nest new nestjs --skip-git --package-manager npm
fi

cd /srv/nestjs
npm install

cd /srv/nestjs
exec "$@"