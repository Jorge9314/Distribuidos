/* 
Ejemplo de como usar net sockets con Node.js 
*/

var net = require('net');

var server = net.createServer(function(socket){
	socket.write('Echo server \r \n');
	socket.pipe(socket);
});

server.listen(1337, '127.0.0.1');

/*
Connect with a tcp client from the command line using netcat, the *nix
utility for reading and writing across tcp/udp network connections. I've only
used it for debbuging myself

$ netcat 127.0.0.1 1337

you should see:
> Echo server

*/

var client = new net.socket();
client.connect(1337, '127.0.0.1', function(){
	console.log('Received: ' + data);
	client.destroy(); // kill client after server's response
});

client.on('close', function(){
	console.log('Conection closed');
});
