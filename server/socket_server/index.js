const { PORT } = require('./credentials');
var app = require('http').createServer()
let io = require('socket.io')(app)

io.on('connect', (socket) => {
    console.log("new socket")
    console.log(socket.handshake.query)
})

app.listen(PORT, () => {
    console.log('listening to port ' + PORT)
})
