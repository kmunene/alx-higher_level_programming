#!/usr/bin/node
const myArray = process.argv;
const len = myArray.length;
const str = 'is';
if (len === 2) {
  console.log('undefined ' + str + ' ' + myArray[2]);
} else if (len === 3) {
  console.log(myArray[2] + ' ' + str + ' ' + myArray[3]);
} else {
  console.log(myArray[2] + ' ' + str + ' ' + myArray[3]);
}