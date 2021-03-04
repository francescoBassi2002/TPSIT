var express = require('express');
var router = express.Router();


router.get('/controllo_user' , (req, res) => {
    const {username, password} = req.query;
    if (username == "bassi" && password == "ciao"){
        res.end("OK");
    }
})

module.exports = router;