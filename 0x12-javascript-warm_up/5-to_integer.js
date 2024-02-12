#!/usr/bin/node

const argv = process.argv;
const num = Math.floor(argv[2]);
if (isNaN(num)) {
  console.log('Not a number');
} else {
  console.log('My number: ' + num);
}
