#!/usr/bin/env bash
service postgresql start
su - postgres -c "psql postgres -c \"CREATE DATABASE testdb\""
su - postgres -c "psql postgres -c \"CREATE USER test_user WITH PASSWORD 'test_password'\""
su - postgres -c "psql postgres -c \"ALTER ROLE test_user SET client_encoding TO 'utf8'\""
su - postgres -c "psql postgres -c \"ALTER ROLE test_user SET default_transaction_isolation TO 'read committed'\""
su - postgres -c "psql postgres -c \"ALTER ROLE test_user SET timezone TO 'UTC'\""
su - postgres -c "psql postgres -c \"GRANT ALL PRIVILEGES ON DATABASE testdb TO test_user\""

#USER: test_user
#PASSWORD: test_password
#DB: testdb