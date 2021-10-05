const http = require ('http');

const server = http.createServer(function(req, res)
{
    res.write('Hi')
    res.end()
})

server.listen(9000, function(error)
{
    if (error)
        console.log('error', error)
    else
        console.log('listening on port 9000');
})