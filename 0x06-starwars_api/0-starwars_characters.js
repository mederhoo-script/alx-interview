#!/usr/bin/node

const request = require('request');

// Get the movie ID from command line arguments
const movieId = process.argv[2];
// Construct the API endpoint URL for the movie
const movieApiUrl = 'https://swapi-api.hbtn.io/api/films/' + movieId;

let characterUrls = []; // URLs of characters in the movie
const characterNames = []; // Names of the characters

// Fetch the list of character URLs from the movie endpoint
const fetchCharacterUrls = async () => {
    await new Promise(resolve => request(movieApiUrl, (err, res, body) => {
        if (err || res.statusCode !== 200) {
            console.error('Error: ', err, '| StatusCode: ', res.statusCode);
        } else {
            const movieData = JSON.parse(body);
            characterUrls = movieData.characters;
            resolve();
        }
    }));
};

// Fetch the names of characters from the character URLs
const fetchCharacterNames = async () => {
    if (characterUrls.length > 0) {
        for (const url of characterUrls) {
            await new Promise(resolve => request(url, (err, res, body) => {
                if (err || res.statusCode !== 200) {
                    console.error('Error: ', err, '| StatusCode: ', res.statusCode);
                } else {
                    const characterData = JSON.parse(body);
                    characterNames.push(characterData.name);
                    resolve();
                }
            }));
        }
    } else {
        console.error('Error: No characters found for the movie');
    }
};

// Main function to retrieve and print character names
const printCharacterNames = async () => {
    await fetchCharacterUrls();
    await fetchCharacterNames();

    // Print each character name on a new line
    for (const name of characterNames) {
        if (name === characterNames[characterNames.length - 1]) {
            process.stdout.write(name);
        } else {
            process.stdout.write(name + '\n');
        }
    }
};

printCharacterNames();
