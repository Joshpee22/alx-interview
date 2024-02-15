#!/usr/bin/node

/**
 * Prints all characters of a Star Wars movie
 */

const myArgs = process.argv.slice(2);
const request = require('request');
const url = 'https://swapi-api.hbtn.io/api/films/' + myArgs[0];

request(url, async function (error, response, body) {
  if (error) {
    console.error('Error:', error);
    process.exit(1);
  }

  const json = JSON.parse(body);
  const endpoints = json.characters;

  // Use Promise.all for concurrent requests
  await Promise.all(endpoints.map(async (endpoint) => {
    try {
      const characterBody = await new Promise((resolve, reject) => {
        request(endpoint, (error, response, body) => {
          if (error) {
            reject(error);
          } else {
            resolve(body);
          }
        });
      });

      console.log(JSON.parse(characterBody).name);
    } catch (error) {
      console.error('Error fetching character:', error);
    }
  }));
});

