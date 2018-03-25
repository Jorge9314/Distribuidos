// PORT Host app
const PORT = 8009;

var express = require('express');
var path = require('path');

var app = express();
var http = require('http').Server(app);
var io = require('socket.io')(http, {pingTimeout: 30000});

var date = new Date();

io.on('connection', (socket) => {
  console.log(`socket ${socket.id} connected`);

  socket.emit('date', date);

  socket.on('get date', () => {
    socket.emit('date', date);
  })
});

let sendBroadcastDate = () => {
  date = new Date();
  io.sockets.emit('update date', date);
}

setInterval(sendBroadcastDate, 10000);

var clientRouter = express.Router();

clientRouter.get('/client', (req, res) => {
  res.sendFile(path.resolve('templates/client.html'))
});

http.listen(PORT, () => {
  console.log(`iDoctor NodeJS Core up on ${PORT}`);
});

app.use(clientRouter);
