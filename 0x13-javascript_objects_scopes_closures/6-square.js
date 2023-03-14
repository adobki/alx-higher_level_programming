#!/usr/bin/node
const SquareSuper = require('./5-square');
module.exports = class Square extends SquareSuper {
  charPrint (c) {
    let row = '';
    let count = 0;
    let h = this.height;
    const w = this.width;
    if (c === undefined) {
      c = 'X';
    }

    while (h--) {
      while (count++ < w) {
        row += c;
      }
      console.log(row);
      row = '';
      count = 0;
    }
  }
};
