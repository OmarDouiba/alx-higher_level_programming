#!/usr/bin/node
// class Square that defines a square and inherits from Square of 5-square.js.
const Rectangle = require("./5-square");
module.exports = class Square extends Rectangle {
  charPrint(c) {
    if (typeof c === "undefined") {
      super.print();
    } else {
      super.print(c);
    }
  }
};
