#!/usr/bin/node
// script that prints 3 lines: (like 1-multi_languages.js) but by using an array of string and a loop
const arr = ["C is fun", "Python is cool", "JavaScript is amazing"];

let i = 0;
while (i < arr.length) {
  console.log(arr[i]);
  i++;
}
