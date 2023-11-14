#!/usr/bin/node
const size = parseInt(process.argv[2]);

if (isNaN(size)) {
  console.log('Missing size');
} else {
  let square = '';
  for (let k = 0; k < size; k++) {
    for (let m = 0; m < size; m++) {
      square += 'X';
    }
    square += '\n';
  }
  console.log(square.trim());
}
