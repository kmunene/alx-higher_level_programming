#!/usr/bin/node
const [, , firstArg] = process.argv;
let myValue = 0;
let x = 0;

if (firstArg) {
  myValue = parseInt(firstArg, 10);
} else {
  console.log('Missing number of occurrences');
}

while (x < myValue) {
  console.log('C is fun');
  x++;
}