#!/usr/bin/node

/* The required modules have been established here */
const request = require('request');

request
  .get(process.argv[2])
  .on('response', (response) => {
    console.log(response.statusCode);
  });
