#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  let counter = 0;
  for (const item of list) {
    if (item === searchElement) {
      counter++;
    }
  }
  return counter;
};
