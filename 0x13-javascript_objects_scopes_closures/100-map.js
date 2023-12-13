#!/usr/bin/node

const list = require('./100-data').list;
const newList = list.map((e, index) => e * index);
console.log(list);
console.log(newList);
