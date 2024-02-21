#!/usr/bin/node
const request = require('request');
const fs = require('fs');

const argv = process.argv.slice(2);

request(argv[0], (err, res, body) => {
  if (err) {
    return console.log(err);
  }
  fs.writeFile(argv[1], body, 'utf-8', (err) => {
    if (err) {
      return console.log(err);
    }
  });
});
