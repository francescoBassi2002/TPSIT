const http = require('http');
const url = require('url');


var server = http.createServer(function(req, res) {
    res.writeHead(200, {"Content-Type": "text/html"});
    res.write('<!DOCTYPE html>'+
    '<html>'+
    ' <head>'+
    ' <meta charset="utf-8" />'+
    ' <title>Pagina Node.js!</title>'+
    ' </head>'+
    ' <body>'+
    '  <p>Sono un paragrafo <strong>HTML</strong>!</p>'+
    ' </body>'+
    '</html>');
    res.end();
  });
  
  server.listen(8080);