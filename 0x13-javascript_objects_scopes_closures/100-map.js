#!/usr/bin/node
const oldList = require('./100-data').list;
const newList = oldList.map((e, index) => e * index);
console.log(oldList);
console.log(newList);
