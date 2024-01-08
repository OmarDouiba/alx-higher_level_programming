#!/usr/bin/node
// script that prints two arguments passed to it, in the following format: “ is ”
const argv = process.argv.slice(2);

if (!isNaN(argv)) {
  console.log(`${typeof argv[0]} is ${typeof argv[1]}`);
} else if (argv.length === 1) {
  console.log(`${argv[0]} is ${typeof argv[1]}`);
} else {
  console.log(`${argv[0]} is ${argv[1]}`);
}
