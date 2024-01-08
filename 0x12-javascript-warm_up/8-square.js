#!/usr/bin/node
// script that prints a square
const argv = process.argv.slice(2);
const n = parseInt(argv[0]);

if (!isNaN(n)) {
  for (let i = 0; i < n; i++) {
    let str = '';
    for (let j = 0; j < n; j++) {
      str += 'X';
    }
    console.log(str);
  }
} else {
  console.log('Missing size');
}
