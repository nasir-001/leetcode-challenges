const express = require("express");
const app = express();

const isSecretWord = word => {
  if (word.length !== 4) return false;
  return /^[aeiou][aeiou][bcdfghjklmnpqrstvwxyz][bcdfghjklmnpqrstvwxyz]$/i.test(word);
};

app.use(express.json());

app.post('/secret-words', (req, response) => {
  if (!req.body.hasOwnProperty('wordsBox')) {
    return response.status(400).json("wordsBox is mandatory, it should have at least 4 words of 4 letters each")
  }
  const { wordsBox } = req.body;
  
  // Validate input
  if (!wordsBox) {
    return response.status(400).json('wordsBox is mandatory, it should have at least 4 words of 4 letters each');
  }
  if (wordsBox.some(word => !/^[a-z]{4}$/.test(word))) {
    return response.status(400).json('Only lower case letters are allowed');
  }
  if (wordsBox.some(word => word.length !== 4)) {
    return response.status(400).json('Each word should have at least 4 letters');
  }
  if (wordsBox.some(word => word.length < 4)) {
    return response.status(400).json('Each word should have at least 4 letters');
  }
  if (wordsBox[0].length !== wordsBox.length) {
    return response.status(400).json('The box must have the same number of rows and columns');
  }

  // Find secret words
  const secretWords = wordsBox.filter(isSecretWord);

  if (secretWords.length > 0) {
    return response.status(200).json({ count: secretWords.length, secretWords });
  } else {
    return response.status(404).json({ count: 0, secretWords: [] });
  }
});

module.exports = app; 
