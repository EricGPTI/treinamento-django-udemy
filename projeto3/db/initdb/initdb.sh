#!/bin/bash
DB_NAME="fusion"
DB_USER="fusion"
DB_PASSWORD="fusion"

if [ -f "/var/lib/postgresql/data/.db_initialized" ]; then
    echo "Database already initialized"
    exit 0
fi 

psql -v ON_ERROR_STOP=1 --username "$POSTGRES_USER" <<-EOSQL
    CREATE DATABASE $DB_NAME;
    CREATE USER $DB_USER WITH PASSWORD '$DB_PASSWORD';
    GRANT ALL PRIVILEGES ON DATABASE $DB_NAME TO $DB_USER;
EOSQL

touch /var/lib/postgresql/data/.db_initialized

echo "Database initialized"