#!/usr/bin/node

const argv = process.argv.slice(2);

const elements = parseInt(argv[0]);

if (isNaN(elements)) {
  console.log('Not a number');
} else {
  console.log(`My number: ${elements}`);
}
