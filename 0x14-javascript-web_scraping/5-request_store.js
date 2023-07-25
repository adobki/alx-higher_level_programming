#!/usr/bin/node
// Gets the contents of a given webpage.

const url = process.argv[2];
const path = process.argv[3];
const request = require('request');
request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    const fp = require('fs');
    fp.writeFile(path, body, function (error) {
      if (error) {
        console.log(error);
      }
    });
  }
});
