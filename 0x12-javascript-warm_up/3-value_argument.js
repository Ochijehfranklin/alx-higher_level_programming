#!/usr/bin/node

const arg1 = process.argv[2] === process.argv[1] ? 'No argument' : process.argv[2];

console.log(arg1);
