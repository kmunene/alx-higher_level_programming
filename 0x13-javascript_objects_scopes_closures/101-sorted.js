#!/usr/bin/node
const myDict = require('./101-data').dict;

const newDict = {};

for (const userId in myDict) {
  const occurrence = myDict[userId];

  if (newDict[occurrence] === undefined) {
    newDict[occurrence] = [userId];
  } else {
    newDict[occurrence].push(userId);
  }
}

console.log(newDict);
