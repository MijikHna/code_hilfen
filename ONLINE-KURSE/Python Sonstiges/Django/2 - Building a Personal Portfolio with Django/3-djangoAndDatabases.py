#1-Creating the models in DjangoTemplates
    #DB um Jobs zu speichern
    #Model = Klasse, die in DB gepeichert wird:
        #in /portfolio-project/models.py erstellen <- kann man mehrer Classen erstellen.

#2-Postgres setup for Django:
    #per Default steht in setttings.py welche DB genutzt wird
    #Postgres:
        #installiert
        #sudo su - postgres  = sich als user postgres anmelden
        #psql = sich mit DB verbinden
        #\conninfo = Verbindungsinfo anzeigen
        #\password postgres  = Passwort für User postgres vergeben/ändern
        #als user postgres -> creatdb dbname = DB erstellen
        #als user postgres -> dropdb dbname = DB löschen

#3-Connecting your Django project to Postgres:
    #bei settings.py noch Postgres einfügen:
        #in DATABASE
        #'default': {
        #    'ENGINE': 'django.db.backends.postgresql',
        #    'NAME': 'portfoliodb',
        #    'USER': 'postgres',
        #    'PASSWORD': 'postgres',
        #    'HOST': 'localhost',
        #    'PORT': '5432',
        #}
    #damit Django sich mit Postgres verbinden kann bracht er psycopg2-binary =>:
        #pip3 install psycopg2-binary

#4-Make Django migrations and migrate:
    #Migrationen = Wege um DB für Django-Projekte zu setzen
        #python3 manage.py makemigrations  = Ausführen, wenn man Änderungen im Model macht.
        #python3 manage.py migrate = die Migrationen ausführen

#5-Setting up an admin panel in Django:
    #Um sich in localhost\admin anmelden zu können => zuerste admin-user erstellen
    #python3 manage.py createsuperuser
    #admin -> django1234

#6-Creating model objects via the admin panel in Django:
    #der Admin der APPP (nicht des Projects) verwaltet das Model =>
    #admin.py öffnen und
        #form .models import Jobs  = Klasse Jobs aus models.py einbinden
        #admin.site.register(Jobs)  = den Admin über die Jobs-Klasse wissen lassen


#7-Pulling objects from the database in Django:
    # = in view.py Code schreiben, um Jobs anzuzeigen
