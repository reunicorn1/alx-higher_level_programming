#!/usr/bin/node

const request = require('request');

request.get(process.argv[2], (err, response, body) => {
  if (err) throw err;
  const data = JSON.parse(body);
  const obj = {};
  data.forEach((element) => {
    if (element.completed === true) {
      if (!Object.prototype.hasOwnProperty.call(obj, element.userId)) {
        obj[element.userId] = 1;
      } else {
        ++obj[element.userId];
      }
    }
  });
  console.log(obj);
});
