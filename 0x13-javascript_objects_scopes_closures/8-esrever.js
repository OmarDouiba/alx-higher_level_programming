#!/usr/bin/node
// function that returns the reversed version of a list.
exports.esrever = function (list) {
  let i = list.length - 1;
  const newList = [];

  while (i > -1) {
    newList.push(list[i]);
    i--;
  }
  return newList;
};
