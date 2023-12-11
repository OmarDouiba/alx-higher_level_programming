#!/usr/bin/node

const argv = process.argv.slice(2);

const element = parseInt(argv[0]);

if (isNaN(element)) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < element; i++) {
    console.log('C is fun');
  }
}
