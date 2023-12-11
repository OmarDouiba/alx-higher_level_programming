#!/usr/bin/node

const argv = process.argv.slice(2);

function secondBiggest(listOfNumbers) {
  if (listOfNumbers <= 1 || isNaN(listOfNumbers)) {
    console.log(1);
  } else {
    console.log(parseInt(listOfNumbers));
  }
}

secondBiggest(...argv);
