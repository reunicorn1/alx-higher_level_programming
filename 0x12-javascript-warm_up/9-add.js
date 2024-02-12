#!/usr/bin/node

function add (a, b) {
  return (a + b);
}
const argv = process.argv;
const num1 = Math.floor(argv[2]);
const num2 = Math.floor(argv[3]);
console.log(add(num1, num2));
