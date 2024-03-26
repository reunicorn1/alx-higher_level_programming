#!/usr/bin/node

/* The required modules have been established here */
const fs = require('fs');

fs.readFile(`./${process.argv[2]}`, 'utf8', (err, data) => {
  if (err) {
    console.log(err);
  } else {
    console.log(data);
  }
});
