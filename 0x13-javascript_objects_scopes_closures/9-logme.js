#!/usr/bin/node

exports.logMe = (function (item) {
  let count = 0;

  const func = (item) => {
    console.log(`${count}: ${item}`);
    count++;
  };
  return func;
}());
