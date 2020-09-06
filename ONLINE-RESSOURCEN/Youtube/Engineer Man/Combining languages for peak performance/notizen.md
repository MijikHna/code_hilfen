### Notizen
* ist möglich, da diese Sprachen Binaries produzieren
* der Aufruf der Binary aus einer Sparche kostet aber auch Zeit. Abwägen, wann es sich lohnt.
#### C
* `gcc -c -fPIC main.c -o main.o` - produziert ein .o (Object-Datei) daraus
* `gcc main.o -shared -o main.so` - Shared Object = Shared Libary  
#### C++  
* `g++ -c -fPIC main.c -o main.o` - produziert ein .o (Object-Datei) daraus
* `g++ main.o -shared -o main.so` - Shared Object = Shared Libary
#### GO
* go build -o main.so -buildmode=c-shared main.go
#### von Python nach JS mittels Pipe
* wer zuerst in die Pipe schreibt, deren Daten werden in der Pipe bleiben, bis jemand die Pipe ausliest, dann ist die Pipe wieder zum Schreiben offen