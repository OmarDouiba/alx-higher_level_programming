#!/usr/bin/node

const argv = process.argv.slice(2);

function add (a, b) {
  console.log(a + b);
}

add(parseInt(argv[0]), parseInt(argv[1]));
