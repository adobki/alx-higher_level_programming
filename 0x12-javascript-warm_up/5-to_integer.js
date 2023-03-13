#!/usr/bin/node
if (process.argv.length < 3) {
  console.log('Not a number');
} else {
  const intStr = Number(process.argv[2]);
  if (isNaN(intStr)) {
    console.log('Not a number');
  } else {
    console.log(`My number: ${intStr}`);
  }
}
