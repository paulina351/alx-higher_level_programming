#!/usr/bin/node
const firstArg = process.argv[2];
const numInt = Number(firstArg);

if (Number.isNaN(numInt)) {
  console.log('Not a number');
} else {
  console.log(`My number: ${Math.floor(numInt)}`);
}
