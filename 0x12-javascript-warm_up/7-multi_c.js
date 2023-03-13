#!/usr/bin/node
if (process.argv.length < 3 || isNaN(Number(process.argv[2]))) {
  console.log('Missing number of occurrences');
} else {
  let count = Number(process.argv[2]);
  const myStr = 'C is fun';
  while (count-- > 0) {
    console.log(myStr);
  }
}
