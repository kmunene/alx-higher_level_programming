#!/usr/bin/node
function add (a, b) {
    return (a + b);
  }
  
  let x;
  let y;
  const myArray = process.argv;
  const len = myArray.length;
  
  if (len <= 3) {
    console.log('NaN');
  } else {
    x = parseInt(myArray[2], 10);
    y = parseInt(myArray[3], 10);
    console.log(add(x, y));
  }