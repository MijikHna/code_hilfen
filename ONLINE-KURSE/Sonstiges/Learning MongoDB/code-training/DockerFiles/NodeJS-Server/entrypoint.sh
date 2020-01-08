sleep 5

if [ ! -f /app/code/mongodb/checks/erledigt.txt ]
then
    cd /app/code/mongodb
    npm install
    
    cd /app/code/mongodb/checks/
    touch erledigt.txt
    echo "alles installiert" > erledigt.txt
else
    echo "alles Notwendige ist installiert"
fi

cd /app/code/mongodb
npm start
