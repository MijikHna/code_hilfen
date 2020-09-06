import sys

# std-Lib imports
''''
import time
dann time.time() benutzen statt time
'''
from time import time

from flask import Flask, request

# meine Impports

# sowas wie DB
messages = [
    {
        "username": "Jack",
        "text": "Hello",
        "time": time()
    },
    {
        "username": "Mary",
        "text": "Hi Jack",
        "time": time()
    }
]

users ={
    'Jack': '1234',
    'Mary': '4321'
}


app = Flask(__name__)


def main():
    # print("flaskApp: " + __name__)
    # print("hilfeLektion1: " + Z_Hilfen.__name__)
    # print("Testen Debug-Mode")

    Flask.debug = True
    Flask.env = 'development'
    app.run()


@app.route("/")
def hello_view():
    return "<h1>Python Messenger<h1>"


'''
da per Default ist GET, Client sendet aber POST
@app.route("/send")
'''


@app.route("/send", methods=['POST'])
def send_view():
    """
    Message senden
    :param: {
        "usenname": str,
        "text": str
    }
    :return: {"ok": true}
    """
    # data = request.json()
    data = request.json
    username = data["username"]
    password = data["password"]
    text = data["text"]

    if username not in users or users[username] != password:
        return {"ok": False} #eigentlich 403
    #elif users[username] != password:
    #    return {"ok": False}

    messages.append({
        "username": username,
        "text": text,
        "time": time()
    })

    return {"ok": True}  # ohne return gibt es Error


@app.route("/messages", methods=['GET'])
def messages_view():
    """
    alle Messages bekommen
    :param: after - Zeit
    :return: {
        "messages": [
        {"username": "str", "text": "str, "time": float},
        ...
        ]
    }
    """
    after = float(request.args['after'])

    # Variante 1:
    newMessages01 = []
    for message in messages:
        if message["time"] > after:
            newMessages01.append(message)

    # Variante 2: List-Comprehensions
    newMessages02 = [message for message in messages if message['time'] > after]

    return {"messages": newMessages02}  # ohne return gibt es Error

@app.route("/auth", methods=['POST'])
def auth_view():
    """
    User authorisieren
    :param: {
        "usenname": str,
        "text": str
    }
    :return: {"ok": true}
    """
    data = request.json
    username = data["username"]
    password = data["password"]
    #text = data["text"]

    if username not in users:
        users[username] = password
        return {"ok": True}
    elif users[username] != password:
        return {"ok": False}
    else:
        return {"ok": True}  # ohne return gibt es Error


def checkUser():
    pass


if __name__ == '__main__':
    main()
