// COLORIZE WORDLE

const WORD_LENGTH = 5;

const colorizeWordle = (guessedWord, hiddenWord) => {
  const colors = Array(WORD_LENGTH).fill(null);
  const indicesOfIncorrectLettersInGuess = [];
  const targetLetters = {};

  for (let i = 0; i < WORD_LENGTH; ++i) {
    let targetLetter = hiddenWord[i];

    if (targetLetter in targetLetters) {
      targetLetters[targetLetter]++;
    } else {
      targetLetters[targetLetter] = 1;
    }

    if (guessedWord[i] === targetLetter) {
      colors[i] = "G";
      targetLetters[targetLetter]--;
    } else {
      indicesOfIncorrectLettersInGuess.push(i);
    }
  }

  for (const i of indicesOfIncorrectLettersInGuess) {
    let guessLetter = guessedWord[i];

    if (guessLetter in targetLetters && targetLetters[guessLetter] > 0) {
      colors[i] = "Y";
      targetLetters[guessLetter]--;
    } else {
      colors[i] = "B";
    }
  }

  return colors.join("");
};
