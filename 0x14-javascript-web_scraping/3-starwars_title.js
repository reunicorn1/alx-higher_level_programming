#!/usr/bin/node

/* The required modules have been established here */
const request = require('request');

request.get(`https://swapi-api.alx-tools.com/api/films/${process.argv[2]}`, (err, response, body) => {
  if (err) throw err;
  const starwarsTitle = JSON.parse(body);
  console.log(starwarsTitle.title);
});
