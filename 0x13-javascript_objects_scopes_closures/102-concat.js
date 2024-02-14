#!/usr/bin/node
const argv = process.argv;
let dataStored = '';
const fs = require('fs');

fs.readFile(argv[2], 'utf8', (err, data) => {
  if (err) {
    return;
  }
  dataStored = data.concat(dataStored);
  fs.readFile(argv[3], 'utf8', (err, data) => {
    if (err) {
      return;
    }
    dataStored = dataStored.concat(data);
    fs.writeFile(argv[4], dataStored, (err) => {
      if (err) {
        console.error(err);
      }
    });
  });
});

// We're telling the program to only read again and finally write the file after it has finished first read and second read. --callback Hell--
