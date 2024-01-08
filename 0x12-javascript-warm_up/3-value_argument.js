#!/usr/bin/node
// script that prints the first argument passed to it.
const argv = process.argv.slice(2);

if (!isNaN(argv)) {
  console.log("No argument");
} else {
  for (let i = 0; i < argv.length; i++) {
    console.log(argv[i]);
  }
}
