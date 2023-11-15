#!/usr/bin/node
const ParSqr = require('./5-square');

class Square extends ParSqr {
  charPrint (c) {
    const char = c || 'X';

    for (let k = 0; k < this.height; k++) {
      console.log(char.repeat(this.width));
    }
  }
}
module.exports = Square;
