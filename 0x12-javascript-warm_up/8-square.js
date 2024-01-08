#!/usr/bin/node
// script that prints a square
const argv = process.argv.slice(2);
const n = parseInt(argv[0]);
let str = '';

if (!isNaN(n)) {
  for (let i = 0; i < n; i++) {
    for (let j = 0; j < n; j++) {
      str += 'X';
    }
    if (i !== n - 1) str += '\n';
  }
  console.log(str);
} else {
  console.log('Missing size');
}
