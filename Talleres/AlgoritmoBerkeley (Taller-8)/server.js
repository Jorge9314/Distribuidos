// PORT Host app
const PORT = 8010;

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

// Initialization client's counter
var numClients = 0;

// Initialization dates to send clients
var dates = [];

// On io detect a socket connection
io.on('connection', (socket) => {

  // Print ID Socket connected
  console.log(`socket ${socket.id} connected`);
  // Update 1 numClients counter
  numClients += 1;

  // When a client goes
  socket.on('disconnect', () => {
    // Reduce 1 numClients counter
    numClients -= 1;
  })

  // Client send a date
  socket.on('take date', date => {
    // Add date to dates
    // @param date -> String
    // @function -> Convert date(String) to date(Object Date)
    dates.push(new Date(date));

    // If all clients send their date
    if (dates.length === numClients) {
      // Process dates
      processDate();
    }
  });
});

// @function -> Get a mean date
let processDate = () => {
  date = new Date;

  // Get means
  date.setDate(meanDays(dates));
  date.setFullYear(meanYear(dates));
  date.setHours(meanHours(dates));
  date.setMinutes(meanMinutes(dates));
  date.setMonth(meanMonths(dates));
  date.setSeconds(meanSeconds(dates));

  // Send new date to all clients
  io.sockets.emit('update date', date);

  // Reset old dates
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
