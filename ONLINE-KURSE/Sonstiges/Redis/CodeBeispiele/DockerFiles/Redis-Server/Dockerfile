FROM debian

WORKDIR /opt

RUN apt update && \
    apt dist-upgrade -y && \
    apt install -y build-essential

ADD http://download.redis.io/releases/redis-5.0.5.tar.gz /opt/

RUN tar xvzf redis-5.0.5.tar.gz && \
    rm redis-5.0.5.tar.gz && \
    cd redis-5.0.5 && \
    make 

COPY ./entrypoint.sh /opt/scripts/entrypont.sh 

VOLUME [ "/app" ]

EXPOSE 6379

ENTRYPOINT [ "/bin/bash", "-c" ]

CMD [ "/opt/scripts/entrypont.sh" ]