FROM debian

WORKDIR /app/code

RUN apt update && \
    apt -y dist-upgrade

RUN apt install -y build-essential git linux-headers-$(uname -r)
RUN apt install -y nodejs npm
RUN npm install -g @angular/cli
COPY ./entrypoint.sh /app/scripts/entrypoint.sh
VOLUME [ "/app/code/" ]
EXPOSE 8000
EXPOSE 4200

ENTRYPOINT [ "/bin/bash", "-c" ]

CMD [ "/app/scripts/entrypoint.sh" ]