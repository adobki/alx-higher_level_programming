#!/usr/bin/node
// Prints all characters of a Star Wars movie by the given movie ID, with
// the results sorted in the original order returned by the API call.
// Javascript has a feature that allows it to run functions asynchronously,
// which causes the array.push() calls for storing the results to be called
// out of order. This led to the results array having a random order that
// changes each time the program is run.
// I accounted for this behaviour by using timers to ensure that each call
// to the getCharacterName function is delayed, causing the results to also
// be returned in the same order in which the function was called.

const movieID = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${movieID}`;
const request = require('request');
const characters = [];

function getCharacterName (url, character) {
  request(url, function (error, response, body) {
    if (error) {
      console.log(error);
    } else {
      characters[character] = JSON.parse(body).name;
    }
  });
}

request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    const movieCharacters = JSON.parse(body).characters;
    movieCharacters.forEach((character) => {
      getCharacterName(character, movieCharacters.indexOf(character));
    });

    // Wait for async calls to getCharacterName return before printing result
    setTimeout(() => {
      characters.forEach((character) => console.log(character));
    }, movieCharacters.length * 200);
  }
});
