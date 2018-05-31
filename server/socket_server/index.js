const { PORT } = require('./credentials');
var app = require('http').createServer();
var io = require('socket.io')(app);
var jwt = require('jsonwebtoken');


io.on('connect', (socket) => {
    // console.log("new socket");
    let token = socket.handshake.query.token
    if (token != undefined) {
        jwt.verify(token, 'secret', { algorithms: ['HS256']}, (err, decoded) => {
            if (err) console.log("invalid token")
            else console.log(decoded)
        });
    }
})

app.listen(PORT, () => {
    console.log('listening to port ' + PORT)
})
