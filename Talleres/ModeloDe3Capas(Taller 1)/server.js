let PORT = 3000;

let app = require('express')();
let http = require('http').Server(app);
let io = require('socket.io')(http);
let path = require('path');

app.get('/client', (req, res) => {
  res.sendFile(path.resolve('templates/client.html'));
});

app.get('/operationalServer', (req, res) => {
  res.sendFile(path.resolve('templates/operationalServer.html'));
});

var operationalServers = {
	sumaServer: null,
	restaServer: null,
	multServer: null,
	divServer: null,
	sqrServer: null,
	sqrtServer: null,
	logServer: null,
};

var client = null;

io.on('connection', (socket) => {

  socket.on('client request', (reservedOperation, num1, num2) => {
  	switch (reservedOperation) {
			case 'suma':
				if (operationalServers.sumaServer === null) {
					socket.emit('server not able');
				} else {
					operationalServers.sumaServer.emit('request', num1, num2, socket.id);
				}
				break;

			case 'resta':
				if (operationalServers.restaServer === null) {
					socket.emit('server not able');
				} else {
					operationalServers.restaServer.emit('request', num1, num2, socket.id);
				}
				break;

			case 'mult':
				if (operationalServers.multServer === null) {
					socket.emit('server not able');
				} else {
					operationalServers.multServer.emit('request', num1, num2, socket.id);
				}
				break;

			case 'div':
				if (operationalServers.divServer === null) {
					socket.emit('server not able');
				} else {
					operationalServers.divServer.emit('request', num1, num2, socket.id);
				}
				break;

			case 'sqr':
				if (operationalServers.sqrServer === null) {
					socket.emit('server not able');
				} else {
					operationalServers.sqrServer.emit('request', num1, num2, socket.id);
				}
				break;

			case 'sqrt':
				if (operationalServers.sqrtServer === null) {
					socket.emit('server not able');
				} else {
					operationalServers.sqrtServer.emit('request', num1, num2, socket.id);
				}
				break;

			case 'log':
				if (operationalServers.logServer === null) {
					socket.emit('server not able');
				} else {
					operationalServers.logServer.emit('request', num1, num2, socket.id);
				}
				break;

			default:
				socket.emit('no valid event');
				break;
  	};
  });

  socket.on('operationalServer response', (result, socketClientID) => {
  	if (client !== null) {
  		client.emit('server response', result);
  	}
  });

  socket.on('set server operation', (reservedOperation) => {
  	switch (reservedOperation) {
			case 'suma':
				if (operationalServers.sumaServer !== null) {
					socket.emit('server not able');
				} else {
					operationalServers.sumaServer = socket;
					socket.emit('server reserved');
				}
				break;

			case 'resta':
				if (operationalServers.restaServer !== null) {
					socket.emit('server not able');
				} else {
					operationalServers.restaServer = socket;
					socket.emit('server reserved');
				}
				break;

			case 'mult':
				if (operationalServers.multServer !== null) {
					socket.emit('server not able');
				} else {
					operationalServers.multServer = socket;
					socket.emit('server reserved');
				}
				break;

			case 'div':
				if (operationalServers.divServer !== null) {
					socket.emit('server not able');
				} else {
					operationalServers.divServer = socket;
					socket.emit('server reserved');
				}
				break;

			case 'sqr':
				if (operationalServers.sqrServer !== null) {
					socket.emit('server not able');
				} else {
					operationalServers.sqrServer = socket;
					socket.emit('server reserved');
				}
				break;

			case 'sqrt':
				if (operationalServers.sqrtServer !== null) {
					socket.emit('server not able');
				} else {
					operationalServers.sqrtServer = socket;
					socket.emit('server reserved');
				}
				break;

			case 'log':
				if (operationalServers.logServer !== null) {
					socket.emit('server not able');
				} else {
					operationalServers.logServer = socket;
					socket.emit('server reserved');
				}
				break;

			default:
				socket.emit('no valid event');
				break;
  	};
  });

  socket.on('set client', () => {
  	client = socket;
  	console.log(`Client: ${socket.id}`);
  });

  socket.on('disconnect', () => {
  	if (operationalServers.sumaServer != null 
  		&& operationalServers.sumaServer.id === socket.id) {
  		operationalServers.sumaServer = null;
  	}
		if (operationalServers.restaServer != null 
			&& operationalServers.restaServer.id === socket.id) {
			operationalServers.restaServer = null;
		}
		if (operationalServers.multServer != null 
			&& operationalServers.multServer.id === socket.id) {
			operationalServers.multServer = null;
		}
		if (operationalServers.divServer != null 
			&& operationalServers.divServer.id === socket.id) {
			operationalServers.divServer = null;
		}
		if (operationalServers.sqrServer != null 
			&& operationalServers.sqrServer.id === socket.id) {
			operationalServers.sqrServer = null;
		}
		if (operationalServers.sqrtServer != null 
			&& operationalServers.sqrtServer.id === socket.id) {
			operationalServers.sqrtServer = null;
		}
		if (operationalServers.logServer != null 
			&& operationalServers.logServer.id === socket.id) {
			operationalServers.logServer = null;
		}
  });
});

http.listen(PORT, () => {
  console.log(`Listening on port ${PORT}`);
});