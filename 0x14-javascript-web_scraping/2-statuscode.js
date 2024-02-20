#!/usr/bin/node
const request = require('request');

const argv = process.argv.slice(2);

request(argv[0], (err, res, body) => {
  if (err) {
    return console.log(err);
  }
  return console.log(`code: ${res.statusCode}`);
});
