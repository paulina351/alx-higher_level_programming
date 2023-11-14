#!/usr/bin/node
const numX = parseInt(process.argv[2]);

if (isNaN(numX)) {
  console.log('Missing number of occurences');
} else {
  let x = 0;
  while (x < numX) {
    console.log('C is fun');
    x++;
  }
}
