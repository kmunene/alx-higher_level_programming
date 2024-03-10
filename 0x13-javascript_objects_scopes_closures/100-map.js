#!/usr/bin/node
const mylist = require('./100-data').list;

const newList = mylist.map((num, index) => num * index);

console.log(mylist);
console.log(newList);
