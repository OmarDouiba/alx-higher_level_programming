#!/usr/bin/node

const argv = process.argv.slice(2);
const element = parseInt(argv[0]);

if (isNaN(element)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < element; i++) {
    let str = '';
    for (let j = 0; j < element; j++) {
      str += 'X';
    }
    console.log(str);
  }
}
