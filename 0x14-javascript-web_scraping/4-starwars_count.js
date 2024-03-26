#!/usr/bin/node

/* The required modules have been established here */
const request = require('request');

request.get(process.argv[2], (err, response, body) => {
  if (err) throw err;

  const id = 18;
  let count = 0;
  const data = JSON.parse(body);
  for (const movie of data.results) {
    for (const character of movie.characters) {
      if (character.includes(id)) {
        count++;
      }
    }
  }
  console.log(count);
});
