#!/usr/bin/node
const fs = require('fs');

const [fileName, text] = process.argv.slice(2);
fs.writeFile(fileName, text, 'utf8', err => err && console.log(err.message));
