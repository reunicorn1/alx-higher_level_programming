#!/usr/bin/node

exports.esrever = function (list) {
  const listReversed = [];
  for (let j = (list.length - 1); j >= 0; j--) {
    listReversed.push(list[j]);
  }
  return (listReversed);
};
