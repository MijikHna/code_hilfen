FROM debian


RUN apt update && \
    apt -y dist-upgrade && \
    apt -y install linux-headers-$(uname -r) build-essential&& \
    apt -y install openssh-server && \
    apt -y install vim nano && \
    apt install -y vsftpd

ADD ./userpass.txt /srv/scripte/userpass.txt

RUN addgroup bvs && \
    useradd -g bvs -ms /bin/bash --password bvs100 bvs100 && \
    (echo 'bvs100'; echo 'bvs100') | passwd bvs100
# m = create Homedir, -s = shell
VOLUME [ "/srv/code" ]

ADD ./entrypoint.sh /srv/scripte/entrypoint.sh

ENTRYPOINT [ "/bin/bash", "-c" ]

CMD ["/srv/scripte/entrypoint.sh"]

