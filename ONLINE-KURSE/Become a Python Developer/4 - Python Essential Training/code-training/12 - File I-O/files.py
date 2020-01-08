# 1 - Opening files
print("# -1 ")
#Datei zum Lesen öffnen
#open gibt File-Objekt, File-Objekt ist Iterator
#f = open("test.txt") #Default ist read + text-Modus
f = open("test.txt", "r")
#f = open("test.txt", "w")
#f = open("test.txt", "a")
# es gibt noch + und b/t <- Default ist
for line in f: # line ist ein String
    print(line.rstrip())
# 2 - Text vs. binary mode 
print("\n# -2")
# \n ist Stringende
#Unterschiedliche Mashinen haben andere Represäntation von \n:
# Linux = LF; Macs = CR, Micorosft = CR LF

# 3 - Text files
print("\n# - 3 ")
#Datei in read + text -Modus öffnen
infile = open("test.txt", "rt")
outfile = open("test-copy.txt", "wt")
for line in infile:
    #print schreibt in file <- hier aber file zeigt auf outfile
    #mit fstrip() wird Line-Ende in das Format des OS umgewandelt
    print(line.rstrip(), file = outfile)
    #in outfile eine Zeile schreiben
    outfile.writelines(line)
    print(".", end="", flush=True)
print("\n done.")
infile.close()
outfile.close()


# 4 - Binary files
print("\n# - 4")
#wenn man eine Datei z.B .jpg im Text-Modus öffnet => kommt Error, da es kein Unicode-Encodings gibt für die Zeichen aus .jpg
infile = open("test.txt", "rb")
outfile = open("test-copy2.txt", "wb")
while True:
    buf = infile.read(10240)
    #Wenn Buffer ist nicht leer
    if buf:
        print(buf)
        outfile.write(buf)
        print(".", end = "", flush=True)
    else:
        print(buf)
        break
outfile.close()
infile.close()
print("\nDone.")