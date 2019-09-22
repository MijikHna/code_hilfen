#official Python runtime herunterladen
FROM python

#set WorkingDir
WORKDIR /app

COPY . /app

#Packete nachinstalleiren
RUN pip install --trusted-host pypi.python.org -r requirements.txt

#Post 80 freigeben
EXPOSE 80

#Define environment variable
ENV NAME World

#app.py-Script im Container ausführen:
CMD ["python", "app.py"]