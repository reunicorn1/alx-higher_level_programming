#!/usr/bin/node

function factorial (number) {
  if (isNaN(number) || number === 0) {
    return (1);
  } else {
    return (number * factorial(number - 1));
  }
}
const argv = process.argv;
const num = Math.floor(argv[2]);
console.log(factorial(num));
