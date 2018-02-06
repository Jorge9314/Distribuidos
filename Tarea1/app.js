var http = require('http'),
    fs = require('fs'),
    // NEVER use a Sync function except at start-up!
    index = fs.readFileSync(__dirname + '/index.html');

// Send index.html to all requests
var app = http.createServer(function(req, res) {
    res.writeHead(200, {'Content-Type': 'text/html'});
    res.end(index);
});

// Socket.io server listens to our app
var io = require('socket.io').listen(app);

// Send current time to all connected clients

var sockets = [];

// Emit welcome message on connection
io.on('connection', function(socket) {
    sockets.push(socket);

    // Use socket to communicate with this particular client only, sending it it's own id
    socket.emit('welcome', { message: 'Welcome!', id: socket.id });

    socket.on('message', (msg, idSocket) => {
    	socket.broadcast.emit('message', msg, idSocket);
    });

    socket.on('response a msg', (msg, idSocket) => {
        for (var i = sockets.length - 1; i >= 0; i--) {
            socket = sockets[i];
            if (socket.id === idSocket) {
                socket.emit('msg received', msg);
                break;
            }
        };
    });
});

app.listen(3000, () => {
    console.log('Server Up!!');
});