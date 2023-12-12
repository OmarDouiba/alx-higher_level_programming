#!/usr/bin/node

const Square5 = require('./5-square');

module.exports = class Square extends Square5 {
  charPrint (c) {
    if (c === undefined) {
      this.print();
    } else {
      let str = '';
      for (let i = 0; i < this.width; i++) {
        for (let j = 0; j < this.width; j++) {
          str += c;
        }
        if (i !== this.width - 1) {
          str += '\n';
        }
      }
      console.log(str);
    }
  }
};
