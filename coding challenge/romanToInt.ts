function decode(roman: string): number {
  // define a dictionary of Roman numerals and their corresponding values
  const numerals: { [key: string]: number } = {
    "I": 1,
    "IV": 4,
    "V": 5,
    "IX": 9,
    "X": 10,
    "XL": 40,
    "L": 50,
    "XC": 90,
    "C": 100,
    "CD": 400,
    "D": 500,
    "CM": 900,
    "M": 1000,
  };
  let result = 0;
  // iterate through the string
  let i = 0;
  while (i < roman.length) {
    // if the current character and the next character form a valid Roman numeral, add the corresponding value to the result
    if (i + 1 < roman.length && numerals[roman.substring(i, i + 2)]) {
      result += numerals[roman.substring(i, i + 2)];
      i += 2;
    }
    // otherwise, add the value of the current character to the result
    else {
      result += numerals[roman[i]];
      i += 1;
    }
  }
  return result;
}