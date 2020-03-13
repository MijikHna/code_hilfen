### Sockets und TCP
* über Sockets reden Prozesse auf dem Rechner mit einander
* mit TCP kann man Sockets über NW benutzen.
* Ablauf:
    * wenn Server gestartet wird, wird, wird Socket erstellt. Diesem Socket wird Sockert un IP zugeordnet. Socket ist für Betriebssystem und Server eingerichtet
    * Wenn Server hochfährt, sendet Server `accept` an den Socket. Betriebssystem versucht sich mit IP zu verbinden und geht zurück zum Server
    * dann wird Client-Socket erstellt auf dem Server. Server sendet wieder `accept`
    * dann wird `backlog` angeschaltet, wird on BS geregelt = Queue mit allen Clients. Dabei muss man max-Clients einstellen
1. Bei jeder Client-Verbindung Rück-Call dieser Verbindung mit Client-Socket als Param gemacht
```ts
net.createServer()
  .listen(PORT, IP, BACKLOG)
  .on('connection', socket => 
    console.log(`new connection from ${socket.remoteAddress}:${socket.remotePort}`
  )
```
2. über diesen Socket kann man dann Daten vom/an Client erhalten/senden. Dafür wird Erreignis `data` des Sockets benutzt, dem Rück-Call zur Verfügung gestellt wird, der dann `Buffer` vom Client erhält. mit `write` kann man in den Socket schreiben. Mit `end` Socket schließen, sonst `keep-alive`
```ts
socket => socket  
.on('data', buffer => {
    const request = buffer.toString()
    socket.write('hello world')
    socket.end()
```
* mit `curl localhost:3000` kann man dann den Server testen oder mit HTTP-Call bzw. Rest-API
```
GET / HTTP/1.1
Host: localhost:3000 //Key-Value
```

#### Parallelisierung
* momentan werde die Server-Anfragen von einem Prozess bearbeiet d.h. wenn weitere Anfragen kommen, werden sie gequeuet und warten ab, bis vorherigen Anfrage komplett bearbeitet werden.
* Lösung: mit workerpool
```ts
import * as wp from 'workerpool'
const workerpool = wp.pool()

net.createServer()
  .listen(PORT, IP, BACKLOG)
  .on('connection', socket => {
    console.log('new connection')
    socket
      .on('data', buffer => {
        console.log('data')
        workerpool.exec(() => fibonacci(100), []) //exec returnt Promise
          .then(res => {
            socket.write(res)
            console.log('done with connection')
            socket.end()
          })
      })
  })

const fibonacci = (n: number) => (n < 2) ? n
  : fibonacci(n - 2) + fibonacci(n - 1)
```