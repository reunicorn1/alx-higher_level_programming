#!/usr/bin/node
const dict = require('./101-data.js').dict;
function createObject (dict) {
  const obj = {};
  for (const key in dict) {
    const value = dict[key];
    if (!Object.prototype.hasOwnProperty.call(obj, value)) {
      obj[value] = [];
    }
    obj[value].push(key);
  }
  return obj;
}
console.log(createObject(dict));
