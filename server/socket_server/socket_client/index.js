const io = require('socket.io-client')
const jwt = require('jsonwebtoken')

// test token
var token = jwt.sign({ id: '5b0cc12791d9566ba9140a32'}, 'secret', { algorithm: 'HS256'})

var socket = io('http://localhost:8080', {
    query: {
        token: token
    }
});

socket.on('connect', () => {
    console.log('woot')
    socket.disconnect()
})