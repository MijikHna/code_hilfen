import sys

sys.path.append("/media/kirill/WindowsD/Programmieren/Python/Skillbox/Messenger")

# std-Lib imports
from flask import Flask

# meine Impports
import Lektion1_Einfuehrung.Hilfen.hilfeLektion1 as Hilfen


def main():
    print("flaskApp: " + __name__)
    print("hilfeLektion1: " + Hilfen.__name__)
    print("Testen Debug-Mode")

    Flask.debug = True
    Flask.env = 'development'
    app.run()


app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello, World!"


@app.route("/stats")
def stats():
    currentState = Hilfen.getStatus()
    return """
    <div>
        <p> Date: {datum}
        <p> Status: {status}
    </div>
    """.format(datum=currentState["date"], status=currentState["status"])


if __name__ == '__main__':
    main()
