// PORT Host app
const PORT = 8009;

// Require libraries
// Require Express.js
var express = require('express');
// Require path
var path = require('path');
// Require utils
let {
  meanHours,
  meanMinutes,
  meanMonths,
  meanDays,
  meanSeconds,
  meanYear
} = require(path.resolve('utils'));

// Creating webapp
var app = express();
var http = require('http').Server(app);

// Initialization socket admin (io)
var io = require('socket.io')(http, {pingTimeout: 30000});

// Initialization date Server
var date = new Date();

var numClients = 0;

var dates = [];

// On io detect a socket connection
io.on('connection', (socket) => {

  // Print ID Socket connected
  console.log(`socket ${socket.id} connected`);
  numClients += 1;

  socket.on('disconnect', () => {
    numClients -= 1;
  })

  // Send first date from server
  socket.on('take date', date => {
    dates.push(new Date(date));

    if (dates.length === numClients) {
      processDate();
    }
  });
});

let processDate = () => {
  date = new Date;
  date.setDate(meanDays(dates));
  date.setFullYear(meanYear(dates));
  date.setHours(meanHours(dates));
  date.setMinutes(meanMinutes(dates));
  date.setMonth(meanMonths(dates));
  date.setSeconds(meanSeconds(dates));

  io.sockets.emit('update date', date);
  dates = [];
};

// Send date Server to all clients
let sendBroadcastGetDate = () => {
  // Send sendme date to all clients
  io.sockets.emit('sendme date');
}

// Send date to Server event to all clients every 2 seconds
setInterval(sendBroadcastGetDate, 10000);

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
