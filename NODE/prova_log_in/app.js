const express = require('express');
const morgan = require('morgan');
const path = require('path');

port = 3000;

app = express();
app.set('view engine', 'ejs');
app.use(morgan("tiny"));


app.get('/', (req, res) => {
    res.render('index.ejs')
})


app.listen(port, () => {console.log("server is running on http://localhost:" + port)});