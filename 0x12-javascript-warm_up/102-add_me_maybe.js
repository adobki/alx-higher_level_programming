#!/usr/bin/node
const addMeMaybe = function (x, func(...){}) {
  let countr = 0;
  while (countr++ < x) {
    func();
  }
}
