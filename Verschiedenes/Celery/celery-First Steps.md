## First Steps
Danach sollte man **http://docs.celeryproject.org/en/latest/getting-started/next-steps.html#next-steps** hier weiter lernen
Celery is Task Queue.  
Vorgehensweise
1. Message Transport auswählen und installieren (broker)
    * RabbitMQ
    * Redis
    * Weitere Broker
2. Celery Installieren
3. Worker starten und Tasks aufrufen
4. Tasks beobachten

### Choosing a Broker
Celery bracht etwas um Nachrichten zu bekommen/senden. Oft is es Service = Message Broker
1. RabbitMQ
    * `apt isntall -y rabbitmq-server`
    ODER in Docker
    * `docker run -d -p 5462:5462 rabbitmq`
    * Sollte Message `Starting rabbitmq-server: SUCCESS` erscheinen
    * *http://www.rabbitmq.com/download.html*
2. Redis
kann eher zu Datenverlust führen als RabbitMQ  
*http://docs.celeryproject.org/en/latest/getting-started/brokers/redis.html#broker-redis*  
Als Docker laufen lassen `docker run -d -p 6379:6379 redis`
3. Weitere Broker:
    1. Amazon SQS
    2. Zookeeper

### Celery installieren
+ `pip install celery`

### Application
Als erstes braucht man Celery Instance = Celery App. Dafür wird python-Modul **tasks.py** erstellt
```python
from celery import Celery

app = Celery('tasks', broker='pyamqp://guest@localhost//') # tasks = Name derzeitigen Moduls. 
#Benötigt, damit die Namen automatisch generiert werden, 
#wenn Tasks in __main__ - Modul definiert sind;
#broker=... = URL des Message Broker

@app.task
def add(x, y):
    return x + y
```

### Celery worker Server starten
Worker starten mit `celery -A tasks worker --loglevel=info`  
In Production wird man Worker als Daemon starten. => Man muss man dann Tools der Platform nutzen (supervisord (googeln Daemonization = *http://docs.celeryproject.org/en/latest/userguide/daemonizing.html#daemonizing*))  
`celery worker --help` - Hilfe für diese Command schauen. Oder auch `celery help`

### Calling the Task
