#!/usr/bin/node
const add = function (a, b) {
  return Number(a) + Number(b);
};

if (process.argv.length < 4) {
  console.log('NaN');
} else {
  const num = add(process.argv[2], process.argv[3]);
  console.log(`${num}`);
}
