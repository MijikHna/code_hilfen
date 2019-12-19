FROM debian

WORKDIR /app

RUN apt update && \
    apt -y dist-upgrade && \
    apt install -y build-essential git linux-headers-$(uname -r) && \
    apt install -y curl gnupg2

#RUN curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | apt-key add - && \
#    echo "deb https://dl.yarnpkg.com/debian/ stable main" | tee /etc/apt/sources.list.d/yarn.list && \
#    apt update
#RUN apt install -y yarn

# Normale npm installl
RUN apt install -y nodejs npm

#Alternative für Node.js und npm
#RUN apt-get install -y python g++ make && \
#    curl -sL https://deb.nodesource.com/setup_13.x | bash - && \
#    apt-get install -y nodejs

RUN npm install -g @nestjs/cli && \
    echo "Die Version von Nest ist -> $(nest --version)"

COPY ./entrypoint.sh /app/scripts/entrypoint.sh
VOLUME [ "/app/" ]

EXPOSE 3000 4200 8000

ENTRYPOINT [ "/app/scripts/entrypoint.sh" ]

CMD [ "/bin/bash" ]