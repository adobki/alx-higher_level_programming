#!/usr/bin/node
function add (a, b) {
  return Number(a) + Number(b);
}
if (process.argv.length < 4) {
  console.log('NaN');
} else {
  const num = add(process.argv[2], process.argv[3]);
  console.log(`${num}`);
}
