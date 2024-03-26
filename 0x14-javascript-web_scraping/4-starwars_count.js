#!/usr/bin/node


const request = require('request');

const characterId = 18; // Wedge Antilles' character ID
const apiUrl = 'https://swapi-api.alx-tools.com/api/films/';

request(apiUrl, { json: true }, (err, res, body) => {
    if (err) {
        console.error('Error:', err);
        return;
    }

    const moviesWithWedge = body.results.filter(movie =>
        movie.characters.includes(`https://swapi-api.alx-tools.com/api/people/${characterId}/`)
    );

    console.log(`${moviesWithWedge.length}`);
});

