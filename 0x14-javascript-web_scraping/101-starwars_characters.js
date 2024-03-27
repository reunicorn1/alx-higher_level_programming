#!/usr/bin/node

/* The required modules have been established here */
const request = require('request');

function getStarWarsData (url) {
  return new Promise((resolve, reject) => {
    request.get(url, (err, response, body) => {
      if (err) reject(err);
      else resolve(JSON.parse(body));
    });
  });
}

async function fetchCharacterData (urls) {
  if (urls.length === 0) {
    return;
  }

  const characterUrl = urls.shift();
  const characterData = await getStarWarsData(characterUrl);
  console.log(characterData.name);

  await fetchCharacterData(urls);
}

async function main () {
  try {
    const filmUrl = `https://swapi-api.alx-tools.com/api/films/${process.argv[2]}`;
    const starWarsFilmData = await getStarWarsData(filmUrl);
    const characterUrls = starWarsFilmData.characters;

    await fetchCharacterData(characterUrls);
  } catch (err) {
    console.error(err);
  }
}

main();
