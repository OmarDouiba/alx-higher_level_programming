#!/usr/bin/node

const argv = process.argv.slice(2);

function secondBiggest (listOfNumbers) {
  const arr = [];
  for (let i = 0; i < listOfNumbers.length; i++) {
    arr.push(parseInt(listOfNumbers[i]));
  }
  const maxNum = Math.max(...arr);
  rem = arr.indexOf(maxNum)
  arr.splice(rem, 1)
  if (listOfNumbers.length <= 1) {
    console.log(0);
  }
  
  console.log(Math.max(...arr));
}

secondBiggest(argv);
