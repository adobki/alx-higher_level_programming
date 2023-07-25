#!/usr/bin/node
// Reads and prints the contents of a given file.

const path = process.argv[2];
const fp = require('fs');
fp.readFile(path, 'utf8', function (error, data) {
  if (error) {
    console.log(error);
  } else {
    console.log(data);
  }
});
