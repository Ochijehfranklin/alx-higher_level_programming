#!/usr/bin/node
const fs = require('fs');

// Directly use the file path from the command line arguments
fs.readFile(process.argv[2], 'utf-8', (err, data) => {
  if (err) console.error('An error occurred:', err);
  else console.log(data);
});
