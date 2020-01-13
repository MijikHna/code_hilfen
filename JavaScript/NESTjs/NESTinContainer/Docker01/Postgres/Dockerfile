FROM debian

WORKDIR /app

RUN apt update && \
    apt -y dist-upgrade && \
    #apt install -y linux-headers-$(uname -r) && \
    apt install -y build-essential git  && \
    apt install -y curl gnupg2 wget

#install PostgresQL
RUN touch /etc/apt/sources.list.d/pgdg.list && \
    echo "deb http://apt.postgresql.org/pub/repos/apt/ buster-pgdg main" >> /etc/apt/sources.list.d/pgdg.list && \
    wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | apt-key add - && \
    apt-get update && \
    apt-get -y install postgresql-11

RUN apt autoremove -y

COPY ./entrypoint.sh /scripts/entrypoint.sh

COPY ./setUpDB.sh /scripts/setUpDB.sh

RUN /bin/bash /scripts/setUpDB.sh

EXPOSE 5432

ENTRYPOINT [ "/scripts/entrypoint.sh" ]

CMD [ "tail", "-f", "/var/log/postgresql/postgresql-11-main.log" ] 
#CMD [ "/bin/bash" ]