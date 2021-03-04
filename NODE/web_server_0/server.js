var http = require('http');
const url = require('url');

var server = http.createServer((req, res) => {
    
    res.writeHead(200 , {"Content-Type" : "text/plain"});
    var page = url.parse
    if (req.url == "/"){
        res.write("Sei nella home");
    }else if (req.url == "/basement"){
        res.write("Sei nella basement");
    }else if (req.url == "/secret"){
        res.write("Sei nella secret req.url");
    }else{
        res.writeHead(404);
        res.write("Pagina non esistente");
    }


    res.end();
})

server.listen(8080);