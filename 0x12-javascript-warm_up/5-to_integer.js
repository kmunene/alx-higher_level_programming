#!/usr/bin/node
const argument = process.argv[2];

if (argument) {
  const integerValue = parseInt(argument, 10);

  if (!isNaN(integerValue)) {
    console.log('My number:', integerValue);
  } else {
    console.log('Not a number');
  }
} else {
  console.log('Not a number');
}