const config=require('dotenv').config({path:__dirname+'/config.env'});
const express = require('express');
const bodyParser = require('body-parser');
const routes = require('./router/api');

var app = express();
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({extended:true}));
app.get('/',(req,res)=>{ 
    res.send("Hi");
});
app.use('/api'+process.env.TOKEN,routes);
app.listen(3000);
