function removeAlmostEqualCharacters(word) {
  let ops = 0;
  let idx = 0;
  while (idx < word.length) {
    charCode = word.charCodeAt(idx);
    nextCharCode = word.charCodeAt(idx + 1);
    if (Math.abs(charCode - nextCharCode) <= 1) {
      ops++;
      idx += 2;
    } else {
      idx += 1;
    }
  }

  return ops;
}

// Input: word = "aaaaa"
// Output: 2

// Input: word = "abddez"
// Output: 2

// Input: word = "zyxyxyz"
// Output: 3

console.log(removeAlmostEqualCharacters("zyxyxyz"));
