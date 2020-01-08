#!/usr/bin/env bash
service postgresql start

echo "alles jut: POSTGRESQL wird gestartet"
echo "Exec macht: $@"
exec "$@"
