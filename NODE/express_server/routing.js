var express = require('express');
var app = express();

app.get('/', function(req, res) {
  res.setHeader('Content-Type', 'text/plain');
  res.end('Sei nella Reception. Posso aiutarti?');
});

app.get('/basement', function(req, res) {
  res.setHeader('Content-Type', 'text/plain');
  res.end('Sei nella cantina dei vini. Le bottiglie sono mie!');
});

app.get('/floor/:floornum/bedroom', function(req, res) {
  res.render('bedroom.ejs', {floor: req.params.floornum});
});

app.use(function(req, res, next){
  res.setHeader('Content-Type', 'text/plain');
  res.send(404, 'La pagina non esiste amico!');
});

app.listen(8080);