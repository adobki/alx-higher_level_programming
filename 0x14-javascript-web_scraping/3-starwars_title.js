#!/usr/bin/node
// Prints the title of a Star Wars movie where the episode number matches a given integer.

const movieID = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${movieID}`;
const request = require('request');
request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    console.log(JSON.parse(body).title);
  }
});
