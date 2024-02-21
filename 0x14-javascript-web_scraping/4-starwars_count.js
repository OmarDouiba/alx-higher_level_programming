#!/usr/bin/node
const request = require('request');

const argv = process.argv.slice(2);

request(argv[0], (err, res, body) => {
  if (err) {
    return console.log(err);
  }
  const parseBody = JSON.parse(body).results;
  let count = 0;

  parseBody.forEach((film) => {
    if (
      film.characters.includes('https://swapi-api.alx-tools.com/api/people/18/')
    ) {
      count++;
    }
  });
  return console.log(count);
});
