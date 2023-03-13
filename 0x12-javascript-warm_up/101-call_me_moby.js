#!/usr/bin/node
const callMeMoby = function (x, func) {
  let countr = 0;
  while (countr++ < x) {
    func;
  }
}
