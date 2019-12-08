FROM debian:stretch

WORKDIR /mongodb

RUN apt update && \
    apt dist-upgrade -y
RUN apt -y install nano wget gnupg2

RUN  apt -y install libcurl3
#apt -y install libcurl4

RUN wget -qO - https://www.mongodb.org/static/pgp/server-4.2.asc | apt-key add - && \
    touch /etc/apt/sources.list.d/mongodb-org.list && \
    echo "deb http://repo.mongodb.org/apt/debian stretch/mongodb-org/4.2 main" | tee /etc/apt/sources.list.d/mongodb-org-4.2.list && \
    apt update && \
    apt install -y mongodb-org mongodb-org-server mongodb-org-shell mongodb-org-mongos mongodb-org-tools

RUN mkdir -p /data/db

EXPOSE 27017
EXPOSE 27018
EXPOSE 27019

VOLUME [ "/mongodb/code" ]

ENTRYPOINT [ "/bin/bash", "-c" ]

CMD ["mongod"]