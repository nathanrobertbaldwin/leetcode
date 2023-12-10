var longestPalindrome = function (s) {
  let freqCounter = {};

  for (let index in s) {
    if (!(s[index] in freqCounter)) freqCounter[s[index]] = 1;
    else freqCounter[s[index]]++;
  }

  let hasOddChar = false;
  for (let letter in freqCounter) {
    if (freqCounter[letter] % 2 === 1) hasOddChar = true;
  }

  let evenSum = 0;
  for (let letter in freqCounter) {
    if (freqCounter[letter] % 2 === 0) evenSum += freqCounter[letter];
    else {
      evenSum += freqCounter[letter] - 1;
    }
  }

  return hasOddChar ? evenSum + 1 : evenSum;
};

console.log(longestPalindrome("bb"));
