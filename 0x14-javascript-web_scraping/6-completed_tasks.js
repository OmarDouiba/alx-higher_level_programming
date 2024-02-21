#!/usr/bin/node
const request = require('request');

const argv = process.argv.slice(2);

request(argv[0], (err, res, body) => {
  if (err) {
    return console.log(err);
  }

  const dic = {};
  const parseBody = JSON.parse(body);

  parseBody.forEach((task) => {
    const userId = task.userId;
    if (dic[userId] === undefined) {
      dic[userId] = 0;
    }
    if (task.completed) {
      dic[userId]++;
    }
  });

  console.log(dic);
});
