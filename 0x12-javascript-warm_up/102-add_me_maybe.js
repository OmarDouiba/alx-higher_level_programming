#!/usr/bin/node
// function that increments and calls a function.
module.exports.addMeMaybe = function (number, theFunction) {
  theFunction(++number);
};
