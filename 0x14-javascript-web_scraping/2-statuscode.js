#!/usr/bin/node
const request = require('request');

// Directly use the URL from the command line arguments
const url = process.argv[2];

// Make a GET request to the provided URL and print the status code
request.get(url, (error, response) => {
  if (error) return console.error('An error occurred:', error.message);
  console.log(`code: ${response.statusCode}`);
});
