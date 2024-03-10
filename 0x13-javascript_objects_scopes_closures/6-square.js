#!/usr/bin/node
const Square = require('./5-square');

class SquareTwo extends Square {
  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    }
    let str = '';
    for (let x = 0; x < this.height; x++) {
      str = '';
      for (let y = 0; y < this.width; y++) {
        str += c;
      }
      console.log(str);
    }
  }
}

module.exports = SquareTwo;
