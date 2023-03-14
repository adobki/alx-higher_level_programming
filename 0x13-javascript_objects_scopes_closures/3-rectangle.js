#!/usr/bin/node
module.exports = class Rectangle {
  constructor (w, h) {
    if (Number(w) > 0 && Number(h) > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    let row = '';
    let count = 0;
    let h = this.height;
    const w = this.width;

    while (h--) {
      while (count++ < w) {
        row += 'X';
      }
      console.log(row);
      row = '';
      count = 0;
    }
  }
};
