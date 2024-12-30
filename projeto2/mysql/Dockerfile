FROM mysql:5.7

WORKDIR /mysql

COPY ./init-db.sh /docker-entrypoint-initdb.d/

RUN chmod +x init-db.sh

RUN apt-get update && apt-get install -y \
    vim \
    iputils-ping \
    net-tools \
    iproute2

EXPOSE 3306