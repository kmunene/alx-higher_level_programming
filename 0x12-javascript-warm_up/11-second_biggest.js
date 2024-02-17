#!/usr/bin/node
const myArray = process.argv.slice(2);

if (myArray.length === 0) {
  console.log(0);
} else if (myArray.length === 1) {
  console.log(0);
} else {
  const sortedArr = myArray.map(Number).sort((a, b) => b - a);
  console.log(sortedArr[1]);
}