#!/usr/bin/node
exports.esrever = function (list) {
  let len = list.length;
  const x = 0;
  const newList = [];

  while (x < len) {
    newList.push(list[len - 1]);
    len--;
  }
  return newList;
};
