FROM debian

WORKDIR /app

RUN apt update && \
    apt -y dist-upgrade && \
    #apt install -y linux-headers-$(uname -r) && \
    apt install -y build-essential git  && \
    apt install -y curl gnupg2 wget

#yarn installieren
RUN curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | apt-key add - && \
    echo "deb https://dl.yarnpkg.com/debian/ stable main" | tee /etc/apt/sources.list.d/yarn.list && \
    apt update && \
    apt install -y yarn

# Normale npm installl
#RUN apt install -y nodejs npm

#install nodejs
RUN curl -sL https://deb.nodesource.com/setup_12.x | bash - && \
    apt update && \
    apt-get install -y nodejs

#install angular
RUN npm install -g @angular/cli && \
    echo "Die Version von Nest ist -> $(ng --version)"

#install synp
RUN npm install -g synp

RUN apt autoremove -y

COPY ./entrypoint.sh /scripts/entrypoint.sh
#COPY ./entrypoint.sh /app/scripts/nodemon-debug.json

VOLUME [ "/app" ]

EXPOSE 4200

ENTRYPOINT [ "/scripts/entrypoint.sh" ]

CMD [ "ng", "serve", "--open", "--host", "\"0.0.0.0\"" ] 
#CMD [ "ng", "serve", "--open", "--port", "8000", "--host", "\"0.0.0.0\"" ] 