#!/usr/bin/node
// Writes a given string to a given file.

const path = process.argv[2];
const data = process.argv[3];
const fp = require('fs');
fp.writeFile(path, data, function (error) {
  if (error) {
    console.log(error);
  }
});
