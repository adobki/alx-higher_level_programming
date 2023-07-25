#!/usr/bin/node
// Prints the number of movies where the character “Wedge Antilles” is present.

const url = process.argv[2];
const character = 18;
let moviesWithCharacter = 0;
const request = require('request');
request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    const movies = JSON.parse(body).results;
    for (const index in movies) {
      const characters = movies[index].characters;
      for (const i in characters) {
        if (characters[i].includes(character)) {
          moviesWithCharacter++;
          // console.log(`Total characters here: ${characters.length}
          // ${movies[index]['title']}: ${characters[i]}`);
        }
      }
    }
    console.log(moviesWithCharacter);
  }
});
