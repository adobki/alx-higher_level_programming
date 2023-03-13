#!/usr/bin/node
const myArray = ['C is fun', 'Python is cool', 'JavaScript is amazing'];
const len = myArray.length;
let idx = 0;
while (idx < len) {
  console.log(`${myArray[idx++]}`);
}
