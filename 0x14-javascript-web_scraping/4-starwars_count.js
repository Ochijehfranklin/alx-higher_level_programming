#!/usr/bin/node

const request = require('request');
const apiUrl = process.argv[2];

request(apiUrl, { method: 'GET' }, (err, { statusCode, body }) => {
  if (err) return console.log(err);
  if (statusCode === 200) {
    const { results } = JSON.parse(body);
    const count = results.map(({ characters }) => {
      const { length } = characters.filter(line => line.includes('18'));
      return length;
    }).reduce((a, b) => a + b);

    console.log(count);
  } else {
    console.log(`Erorr Code: ${statusCode}`);
  }
});