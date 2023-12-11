#!/usr/bin/node

const argv = process.argv.slice(2);

function fact(a) {
    if (isNaN(a) || a === 0) {
        return 1;
    } else {
        return a * fact(a - 1)
    }
}

console.log(fact(parseInt(argv[0])));