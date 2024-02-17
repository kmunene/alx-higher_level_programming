#!/usr/bin/node
const [, , firstArg] = process.argv;
let myValue = 0;
let x;
let y;
let str = '';

if (firstArg) {
  myValue = parseInt(firstArg, 10);
} else {
  console.log('Missing size');
}

if (!isNaN(myValue)) {
  for (x = 0; x < myValue; x++) {
    str = '';
    for (y = 0; y < myValue; y++) {
      str += 'X';
    }
    console.log(str);
  }
} else {
  console.log('Missing size');
}