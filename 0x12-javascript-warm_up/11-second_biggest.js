#!/usr/bin/node
if (process.argv.length < 4) {
  console.log('0');
} else {
  const num = process.argv[2];
  console.log(`${num}`);
}
