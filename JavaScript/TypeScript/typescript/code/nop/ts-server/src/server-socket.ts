import * as net from 'net';
import * as Request from './helpers/request'
import * as Response from './helpers/response'

const PORT = 3000
const IP = '0.0.0.0'
const BACKLOG = 100

net.createServer()
    .listen(PORT, IP, BACKLOG) //Socket-Server erstellen und auf IP horchen
    .on('connection', socket => {
        console.log(`new connection from ${socket.remoteAddress}:${socket.remotePort}`);
        socket.on('data', buffer => {
            const request = buffer.toString();
            //socket.write('hello world');
            let myMap = new Map();
            socket.write(Response.compileResponse({
                protocol: 'HTTP/1.1',
                headers: myMap.set('Content-Type', 'application/text'),
                status: 'OK',
                statusCode: 200,
                body: '<html><body><h1>Greetings</h1></body></html>'
            }));
            socket.end();


        });
    }
    ); //Beobachter-Pattern: connection wird abgehorcht

/*
mit net-package kann man
1. sicht mit Sockets verbinden
2. in/aus Sockets lesen und schreiben
*/