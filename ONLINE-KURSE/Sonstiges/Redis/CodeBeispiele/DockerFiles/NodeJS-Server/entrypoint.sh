sleep 5

if [ ! -f /app/code/redis/checks/erledigt.txt ]
then
    cd /app/code/redis
    npm install --save-dev babel-cli babel-preset-env babel-preset-stage-0
    npm install --save ioredis nodemon
    
    cd /app/code/redis/checks/
    touch erledigt.txt
    echo "alles installiert" > erledigt.txt
else
    echo "alles Notwendige ist installiert"
fi

#PATH=$PATH:/app/code/redis
cd /app/code/redis
npm start
