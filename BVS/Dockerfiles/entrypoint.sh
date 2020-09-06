service ssh start
service vsftpd start

service --status-all

tail -f /var/log/alternatives.log