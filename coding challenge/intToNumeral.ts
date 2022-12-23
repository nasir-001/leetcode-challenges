function intToNumeral(n: number): string {
  // define a dictionary of Roman numerals and their corresponding values
  const numerals = {
    1: "I",
    4: "IV",
    5: "V",
    9: "IX",
    10: "X",
    40: "XL",
    50: "L",
    90: "XC",
    100: "C",
    400: "CD",
    500: "D",
    900: "CM",
    1000: "M",
  };
  let result = "";
  // iterate through the dictionary in reverse order
  for (const [value, numeral] of Object.entries(numerals).reverse()) {
    // while the value of n is greater than or equal to the current value in the dictionary
    while (n >= Number(value)) {
      // add the corresponding Roman numeral to the result
      result += numeral;
      // subtract the value from n
      n -= Number(value);
    }
  }
  return result;
}