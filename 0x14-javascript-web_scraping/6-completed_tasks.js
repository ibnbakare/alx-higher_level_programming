#!/usr/bin/node

const req = require("request");
const url = process.argv[2];

req.get(url,function(err,res,body){
    if (err){
        console.log(err)
    }
    else {
        jobs = JSON.parse(body)
        console.log(jobs.length)
            for (let i = 0; i < jobs.length; i++){
             if (jobs[i]['compeleted'] === true){
                console.log(jobs)
            }
        }
    }
})
