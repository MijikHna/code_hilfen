sleep 5

if [ ! -d /app/code/angular-code/learn-app ]
then
    cd /app/code/angular-code
    ng new learn-app --defaults=true
    cd /app/code/angular-code/learn-app
    npm install jquery --save-dev
    npm install bootstrap --save-dev
fi
cp -R /app/code/angular-code/ANGULAR* /app/code/angular-code/learn-app/src/app
cd /app/code/angular-code/learn-app
ng serve --open --port 8000 --host "0.0.0.0"