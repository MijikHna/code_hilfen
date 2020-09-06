import sys
import threading
from time import time, sleep
import datetime

print(sys.path)
sys.path.append("/media/kirill/WindowsD/Programmieren/Python/Skillbox/Messenger")

from PyQt5 import QtWidgets
import requests

import Lektion3_PyQT.client_ui as clientUI  # ohne as clientUI kann man einfach auf die Klassen und Funktionen direkt zugrifen ohne Klassennamen anzugeben

class ExampleApp(QtWidgets.QMainWindow, clientUI.Ui_MainWindow): #Classen-Ableitung von zwei Klassen
    def __init__(self):  # Konstruktor überschreiben
        super().__init__()  #ruft Konstruktor(-en) der Basiskassen(en)
        self.setupUi(self) # def setupUi(self, MainWindow): ... => beim Auruf wird der erste Parameter weggelassen, da ja self(Zeiger auf sich selbst)
        # über self kann man jetzt auch auf die Eigenschaften der Basis-Klassen zugreifen
        self.pushButton.clicked.connect(self.send) # pushButton.clicked binden an Funktion send() (in google pyqt trigger function onclick

        #refreshMessages als Thread laufen
        threading.Thread(target=self.refreshMessages).start()



    def send(self):
        #print(self.inputMessage.text())
        #self.inputMessage.setText("")
        #self.inputMessage.update()
        #self.inputMessage.repaint() #ganzes Obj updaten

        # self.textBrowser.append("Jack at 15:30")
        # self.textBrowser.append("Hi")
        # self.textBrowser.append("Mari at 15:33")
        # self.textBrowser.append("Hi Jack")
        # #self.textBrowser.update()
        # self.textBrowser.repaint()
        text = self.inputMessage.text()
        self.inputUsername.setText('')
        username = self.inputUsername.text()
        self.inputUsername.setText('')
        password = self.lineEdit_3.text()
        self.lineEdit_3.text()
        print(text + username + password)
        try:
            response = requests.post("http://localhost/login", json={
                "username": username,
                "password": password
            })
            print(response.text)
            response = requests.post("http://localhost/send", json={
                "username": username,
                "password": password,
                "text": text
            })
            print(response.text)
        except Exception: #  oder request.exception.ConnectionError
            print("Server nicht da")
            return
        except: #  alle Exception abfragen
            print("Error passiert")
            return

    def refreshMessages(self):
        # hier eigentlich Code des Recievers
        last_time = 0

        while True:
            try:
                response = requests.get("http://localhost:5000/messages",
                                    params={'after': last_time})  # => http://localhost:5000/messages?after=xxxx
            except:
                print("Error passiert")
                sleep(1)
                continue

            messages = response.json()["messages"]
            for message in response.json()["messages"]:
                beatity_time = datetime.fromtimestamp(message["time"])
                beatity_time = beatity_time.strftime('%d/%m/%Y %H:%M:%S')
                self.textBrowser.append(message["text"])
                self.textBrowser.append(message["username"] + str(message['time']))
                self.textBrowser.append(message["password"])
                #self.textBrowser.repaint() # -> das hat Error verursacht
                #print(message["username"], beatity_time)
                #print(message["text"])

                last_time = message['time']

            time.sleep(1)





if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    window = ExampleApp()
    window.show()
    app.exec_()
