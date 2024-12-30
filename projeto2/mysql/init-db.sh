#!/bin/bash
set -e

mysql -u root -p"$MYSQL_ROOT_PASSWORD" <<-EOSQL
    CREATE DATABASE IF NOT EXISTS projeto2;
    CREATE USER IF NOT EXISTS 'django2'@'%' IDENTIFIED BY 'projeto2';
    GRANT ALL PRIVILEGES ON projeto2.* TO 'django2'@'%';
    FLUSH PRIVILEGES;
EOSQL