#!/usr/bin/node
if (process.argv.length < 3 || isNaN(Number(process.argv[2]))) {
  console.log('Missing size');
} else {
  const count = Number(process.argv[2]);
  let y;
  let x = y = count;
  let row = '';
  while (x-- > 0) {
    while (y-- > 0) {
      row += 'X';
    }
    console.log(`${row}`);
    row = '';
    y = count;
  }
}
