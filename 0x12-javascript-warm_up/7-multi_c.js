#!/usr/bin/node
//  script that prints x times “C is fun”
const argv = process.argv.slice(2);
const n = parseInt(argv[0]);

if (!isNaN(n)) {
  for (let i = 0; i < n; i++) {
    console.log('C is fun');
  }
} else {
  console.log('Missing number of occurrences');
}
