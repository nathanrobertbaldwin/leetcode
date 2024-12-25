function _isPalindrome(s) {
  for (let i = 0; i < Math.floor(s.length / 2); i++) {
    if (s[i] !== s[s.length - 1 - i]) return false;
  }
  return true;
}

function _getStringInfo(s) {
  let dict = {};
  for (let i = 0; i < s.length; i++) {
    if (s[i] in dict) {
      dict[s[i]].push(i);
    } else {
      dict[s[i]] = [i];
    }
  }
}

function longestPalindrome(s) {
  function substringChecker(s, charIdxs, leftIdx, rightIdx) {
    slice = s.slice(charIdxs[leftIdx], charIdxs[rightIdx + 1]);
    if (_isPalindrome(slice)) return charIdxs[rightIdx] - char[leftIdx] + 1;
    else {
      return Math.max(
        substringChecker(s, charIdxs, leftIdx + 1, rightIdx),
        substringChecker(s, charIdxs, leftIdx, rightIdx - 1)
      );
    }
  }


  for (char in dict) {
    let charIdxs = dict[char];
    let left = 0;
    let right = charIdxs[charIdxs.length - 1];
    substringChecker(s, dict[char], left, right);
  }

  return longest;
}

console.log(longestPalindrome("xk30skdjf3j99j03jsl"));
