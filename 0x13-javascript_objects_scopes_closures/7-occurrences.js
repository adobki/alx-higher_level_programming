#!/usr/bin/node
exports.nbOccurences = (list, searchElement) =>
  list.filter(num => num === searchElement).length;
