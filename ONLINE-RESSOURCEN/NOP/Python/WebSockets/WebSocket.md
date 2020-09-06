WebSocket - Kommunikations-Protokoll über TCP um Nachrichten zwischen Browser und Server auszutauschen. mit WebSocket kann man Events beobachten und nur diese Aktualisieren => weniger Ressourcen. Server besteht aus `consumer` und `producer`
* https://nuancesprog.ru/p/6466/

### Requirements
* `pip install websokcets`

### Message - consumer
```python
import asyncio
import logging
import websockets

logging.basicConfig(level=logging.INFO)
async def consumer_handler(websocket: WebSocketClientProtocol) -> None:
    async for message in websocket:
        log_message(message)

async def consume (hostname: str, port: int) -> None:
    websocket_resource_url = f"ws://{hostname}:{port}"
    async with websockets.connect(websocket_resource_url) as websocket:
        await consumer_handler(websocket)
def log_message(message: str) -> None:
    logging.info(f"Message: {message}")

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_util_complete(cunsume(hostname="localhost", port=4000))
    loop.run_forever()
```
* `async/await` - Syntax um mit Promises zu arbeiten. Promise ist in Python ein Objekt für Übergabe oder Abbruch von asynchronen Operationen. 
    * `async` - garantiert, dass die Funktion Promise returnt und nicht-Promise in ein Promise wrappt. Während des Calls kann `await` andren Code ausführen, der nichts mit diesem Prozess zusammen hat
* `websocket_resource_url = f"ws://{hostname}:{port}"` - Protokol ws = WebSocket.
* `async with websockets.connect(websocket_resource_url) as ws:` - öffnen Connection mit WebSocket, dabei wird auf Connection *await*et
    * `async for message in ws` - synchronisierter Prozess für for. ermöglicht asynchronen Iterator
* in main wird consumer starten. Wenn der Server nicht antwortet => 404

### Producer
```py
import asyncio
import websockets

async def produce(message: str, host: str, port: int) -> None:
    async with websockets.connect(f"ws://{host}:{port}") as ws:
        await ws.send(message)
        await ws.recv()

loop = asyncio.get_event_loop()
loop.run_until_compelete(produce(message="hi", host="localhost", port='4000'))

# ODER ab Python 3.7
asyncio.run(produce(message="hi", host="localhost", port='4000'))
```

### Server
Server als Klasse implementiert. Server versendet Messages, die von Producer erstellt wurden
```py
import asyncio
import logging
import websockets
from websockets import WebSocketServerProtocol as wsp

logging.basicConfig(level=logging.INFO)

class Server:
    clients = set()

    async def register(self, ws: wsp) -> None:
        self.clients.add(ws)
        logging.info(f'{ws.remote_address} connect.')

    async def unregister(self, ws: wsp) -> None:
        self.clients.remove(websocket)
        logging.info(f'{ws.remote_address} disconnect.')
    
    async def send_to_clients(self, message: str) -> None:
        if self.clients:
            await asyncio.wait([client.send(message) for client in self.clients])

    async def unregister(self, ws: wsp) -> None:
        await self.register(ws)
        try:
            await self.distribute(ws)
        finally:
            await self.unregister(ws)

    async def distribute(self, ws: wsp) -> None:
        async for message in ws:
            await self.send_to_clients(message)
    
server = Server()
start_server = websockets.serve(server.ws_handler, 'localhost', 4000)
loop = asyncio.get_event_loop()
loop.run_until_complete(start_server)
loop.run_forever()
```
* `websockets.serve` - is Wrapper um `create_server()` - erstellt Server, als Arg = WebSocket
* Wenn Client sich verbindent, wird `WebSocketServerProtocol` erstellt, macht Handshake, gibt Verbindung ans entsprechenden "Bearbeiter". Wenn "Bearbeiter" fertig ist. Server mach Handshake zum Disconnecten
* hier im Bsp: Server fürht nur aus `ws_handler` der Klasse. 
* `ws_handler` - registriert den Client und senden Nachrichten an den Client und schließt Connection. Consumer bleibt verbudnen, Producer wird getrennt.
* Unterprogramm `distribute` wird Messages an WebSocket senden.
* `await asyncio.wait([client.send(message) for client in self.clients])` - garantiert, dass weiterer Code ausgeführt wird, nur wenn alle Clients Message bekommen haben.

### Vorteile WebSockets
1. Anfragen können von beiden Seiten kommen
2. Client und Server sind permanent verbunden