#!/usr/bin/node
const args = process.argv;
if (args.length <= 3) {
  console.log(0);
} else {
  const arr = [];
  for (let i = 2; i < args.length; i++) {
    arr.push(parseInt(args[i]));
  }
  arr.sort();
  arr.reverse();
  console.log(arr[1]);
}
