#!/usr/bin/node
// script that prints My number: <first argument converted in integer> if the first argument can be converted to an integer
const argv = process.argv.slice(2);

if (parseInt(argv[0])) {
  console.log(`My number: ${argv[0]}`);
} else {
  console.log('Not a number');
}
