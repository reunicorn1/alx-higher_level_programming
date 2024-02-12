#!/usr/bin/node

const argv = process.argv;
const num = Math.floor(argv[2]);
if (isNaN(num)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < num; i++) {
    console.log('X'.repeat(num));
  }
}
