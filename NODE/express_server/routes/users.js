var express = require('express');
const app = require('../app');
var router = express.Router();

/* GET users listing. */
router.get('/' , (req, res) => {
  res.render('users.ejs');
})

module.exports = router;
