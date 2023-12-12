#!/usr/bin/node

module.exports = class Rectangle {
  constructor (w, h) {
    this.width = w;
    this.height = h;
  }

  print () {
    for (let i = 0; i < this.height; i++) {
      let str = '';
      for (let j = 0; j < this.width; j++) {
        str += 'X';
      }
      console.log(str);
    }
  }

  rotate () {
    let tmp;
    tmp = this.height;
    this.height = this.width
    this.width = tmp;
  }

  double () {
    this.width = this.width * 2;
    this.height = this.height * 2;
  }
};
