#!/usr/bin/node
// Prints all characters of a Star Wars movie by the given movie ID.

const movieID = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${movieID}`;
const request = require('request');

function getCharactersName (url) {
  request(url, function (error, response, body) {
    if (error) {
      console.log(error);
    } else {
      console.log(JSON.parse(body).name);
    }
  });
}

request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    const movieCharacters = JSON.parse(body).characters;
    movieCharacters.forEach((character) => getCharactersName(character));
  }
});
