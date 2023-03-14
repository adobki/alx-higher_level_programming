#!/usr/bin/node
exports.esrever = function (list) {
  let len = list.length - 1;
  let idx = 0;
  const revList = [];
  while (len >= 0) {
    revList[idx++] = list[len--];
  }
  return revList;
};
