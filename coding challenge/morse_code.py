from typing import List
MORSE_CODE = {
    "E": ".",
    "T": "-",
    "I": "..",
    "A": ".-",
    "N": "-.",
    "M": "--",
    "S": "...",
    "U": "..-",
    "R": ".-.",
    "W": ".--",
    "D": "-..",
    "K": "-.-",
    "G": "--.",
    "O": "---"
}
def possibilities(word: str) -> List[str]:
  if word in MORSE_CODE.values():
    return [key for key, value in MORSE_CODE.items() if value == word]
  else:
    unknown_possibilities = [possibilities(word.replace("?", possibility, 1)) for possibility in [".", "-"]]
    return [item for sublist in unknown_possibilities for item in sublist]