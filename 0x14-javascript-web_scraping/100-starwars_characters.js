#!/usr/bin/node

/* The required modules have been established here */
const request = require('request');

request.get(`https://swapi-api.alx-tools.com/api/films/${process.argv[2]}`, (err, response, body) => {
  if (err) throw err;
  const starwarsdata = JSON.parse(body);
  starwarsdata.characters.forEach((character) => {
    request.get(character, (err, response, body) => {
      if (err) throw err;
      const person = JSON.parse(body);
      console.log(person.name);
    });
  });
});
