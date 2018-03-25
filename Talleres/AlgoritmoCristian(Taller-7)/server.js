// PORT Host app
const PORT = 8009;

// Require libraries
// Require Express.js
var express = require('express');
// Require path
var path = require('path');

// Creating webapp
var app = express();
var http = require('http').Server(app);

// Initialization socket admin (io)
var io = require('socket.io')(http, {pingTimeout: 30000});

// Initialization date Server
var date = new Date();

// On io detect a socket connection
io.on('connection', (socket) => {

  // Print ID Socket connected
  console.log(`socket ${socket.id} connected`);

  // Send first date from server
  socket.emit('date', date);

  // If socket want to get date
  socket.on('get date', () => {
    // Emit a date Server
    socket.emit('date', date);
  })
});

// Send date Server to all clients
let sendBroadcastDate = () => {
  // Update date Server
  date = new Date();
  // Send date Server to all clients
  io.sockets.emit('update date', date);
}

// Send date Server to all clients every 10 seconds
setInterval(sendBroadcastDate, 10000);

// Define router to /client
var clientRouter = express.Router();

// Define method GET to /client
clientRouter.get('/client', (req, res) => {
  // Send client.html (contains socket)
  res.sendFile(path.resolve('templates/client.html'))
});

// Up server on ${PORT}
http.listen(PORT, () => {
  console.log(`Christiam's Algorithm up on ${PORT}`);
});

// Notify to Express to use a clientRouter
app.use(clientRouter);
