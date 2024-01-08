#!/usr/bin/node
// script that prints the addition of 2 integers
const argv = process.argv.slice(2);

function add (a, b) {
  if (isNaN(parseInt(a)) || isNaN(parseInt(b))) {
    console.log('NaN');
  } else {
    console.log(parseInt(a) + parseInt(b));
  }
}

add(argv[0], argv[1]);
