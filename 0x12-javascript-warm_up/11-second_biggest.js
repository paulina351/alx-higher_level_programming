#!/usr/bin/node
const biggestArgs = process.argv.slice(2).map(Number);

if (biggestArgs.length === 0) {
  console.log(0);
} else if (biggestArgs.length === 1) {
  console.log(0);
} else {
  const convertedArgs = biggestArgs.sort((a, b) => b - a);
  console.log(convertedArgs[1]);
}
