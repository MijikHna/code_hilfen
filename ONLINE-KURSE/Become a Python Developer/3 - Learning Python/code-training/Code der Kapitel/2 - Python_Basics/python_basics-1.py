
#1 - Building Hello World
def main():
    print("Hello world")

#Wenn diese Python-Datei geladen wurde und Python-Interpreter hat der Variable __name__ den Wert __main__ vergeben, dann wird dieses Python-Programm als main ausgeführt und main() wird aufgerufen
#diese Zeile hilft zu unterscheiden, ob die Python Datei als main oder als einfaches Python-Programm ausgeführt wird

if __name__ == "__main__":
    main()