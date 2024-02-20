#!/usr/bin/node
const request = require("request");

const argv = process.argv.slice(2);

request(
  `https://swapi-api.alx-tools.com/api/films/${argv[0]}`,
  (err, res, body) => {
    if (err) {
      return console.log(err);
    }
    const parseBody = JSON.parse(body);
    return console.log(parseBody.title);
  }
);
