#!/usr/bin/node
const request = require('request');

const argv = process.argv.slice(2);

request(argv[0], (err, res, body) => {
  if (err) {
    return console.log(err);
  }

  let count;
  const dic = {};
  const parseBody = JSON.parse(body);

  parseBody.forEach((ele) => {
    const id = ele.userId;
    if (dic[id] === undefined) {
      count = 0;
    }
    if (ele.completed) {
      count++;
      dic[id] = count;
    }
  });

  console.log(dic);
});
