function _isPalindrome(s) {
  for (let i = 0; i < Math.floor(s.length / 2); i++) {
    if (s[i] !== s[s.length - 1 - i]) return false;
  }
  return true;
}

// console.log(_isPalindrome("abcba"));

function genMaxRanges(s) {
  let ranges = {};
  for (let i = 0; i < s.length; i++) {
    if (s[i] in ranges) {
      if (ranges[s[i]].length === 1) {
        ranges[s[i]].push(i);
      } else {
        ranges[s[i]][1] = i;
      }
    } else {
      ranges[s[i]] = [i];
    }
  }

  return ranges;
}

function maxProduct(s) {
  let bigPalSubstring = "";
  let nextBigPalSubstring = "";

  function examineSubstrings(s) {
    let maxRanges = genMaxRanges(s);
    for (letter in maxRanges) {
      let letterRange = maxRanges[letter];
      let left = letterRange[0];
      let right = letterRange[1] + 1;
      let subString = s.slice(left, right);
      if (_isPalindrome(subString)) {
        if (subString.length > nextBigPalSubstring.length) {
          nextBigPalSubstring = subString;
        }
        if (subString.length > bigPalSubstring.length) {
          nextBigPalSubstring = bigPalSubstring;
          bigPalSubstring = subString;
        }
      }
    }
  }
  examineSubstrings(s);
  return [bigPalSubstring, nextBigPalSubstring];
}

console.log(maxProduct("accbcaxxcxx"));

// lol whoops
