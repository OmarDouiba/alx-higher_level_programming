#!/usr/bin/node

const argv = process.argv.slice(2);

function secondBiggest (listOfNumbers) {
  const arr = [];
  for (let i = 0; i < listOfNumbers.length; i++) {
    if (isNaN(parseInt(listOfNumbers[i]))) {
      console.log(0);
    }
    arr.push(parseInt(listOfNumbers[i]));
  }
  console.log(arr);
  if (listOfNumbers.length <= 1) {
    console.log(0);
  } else {

  }
  const maxNum = Math.max(arr);
  console.log(maxNum);
}

secondBiggest(argv);
