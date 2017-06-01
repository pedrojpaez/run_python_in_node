var express = require('express')
var app = express()
var path = require('path')
var spawn = require('child_process').spawn

var py = spawn('python', [path.join(__dirname, 'python','test.py')]),
data = {'first': 1, 'second': 2},
dataString = '';

py.stdout.on('data', function(data){
  dataString += data.toString();
});
py.stdout.on('end', function(){
  console.log(dataString);
});
py.stdin.write(JSON.stringify(data));
py.stdin.end();
