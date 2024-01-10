#!/usr/bin/node
// function that returns the reversed version of a list.
exports.esrever = function (list) {
  let i = list.length - 1;
  const new_list = [];

  while (i > -1) {
    new_list.push(list[i]);
    i--;
  }
  return new_list;
};
