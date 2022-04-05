#!/usr/bin/node
const arg = process.argv[2];
function factorial (arg) {
  if (isNaN(arg) || arg === 1) {
    return (1);
  } else {
    return (arg * factorial(arg - 1));
  }
}
console.log(factorial(parseInt(arg)));
