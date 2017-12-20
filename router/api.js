//Dependencies
var express = require('express');
var router = express.Router();
var python = require('python-shell');
//routes
router.route('/')
      .get((req,res)=>{
    // Register new users ---> Frontend
    res.send("Good try");
  })
    .post((req,res)=>{
      var options = {
          mode : 'text',
          args : [req.body.data,process.env.IP_ADDRESS,process.env.PORT]
      };
      python.run('python/kumu.py',options,function(err,results){
          console.log(process.env.PORT);
          if(err) throw err;
          res.send(results);
    });
    //res.send("Ended")
});

module.exports = router;
//Important
/*To exchange data between node.js and python
pyshell.send('super');
pyshell.on('message',function(message){
    res.send(message);
});
pyshell.on('end',function(err){
    if(err) throw err;
    console.log('finished');
});
python.run('kumu.py',function(err,results){
    if(err) res.send(err);
    res.send(results);
});*/
/*
Authentication & User tasks on Mongodb
@deprecated
router.route('/users')
        .post(function(req,res){
            var user = new User();
            user.name = req.body.name;
            user.save(function(err) {
                if (err) res.send(err);
        // Use python-shell to generate deep learning responses
            res.send('User created!' );
            });

        })

        .get(function(req,res){
            User.find(function(err, users) {
                if (err)
                    res.send(err);

                res.json(users);
            });
        });

router.route('/users/:user_id')
        .get(function(req,res){
            User.findById(req.params.user_id,function(err,user){
                if(err)
                    res.send(err);
                res.json(user);
            });
        })
        .put(function(req,res){
            User.findById(req.params.user_id,function(err,user){
                if(err)
                    res.send(err);
                user.name = req.body.name;

                user.save(function(err){
                    if(err)
                        res.send(err);
                    res.send('User Updated');
                });
            });
        })
        .delete(function(req,res){
            User.remove({
                _id: req.params.user_id
            }, function(err,user){
                if(err)
                    res.send(err);
                res.json({message:'Successfully deleted'});

            });
        });*/
//Module Exports
