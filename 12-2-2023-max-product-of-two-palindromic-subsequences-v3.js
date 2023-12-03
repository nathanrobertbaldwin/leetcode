function _getStringInfo(s) {
  let ranges = {};
  let uniqueLetters = 0;

  for (let i = 0; i < s.length; i++) {
    if (s[i] in ranges) {
      if (ranges[s[i]].length === 1) {
        ranges[s[i]].push(i);
      } else {
        ranges[s[i]][1] = i;
      }
    } else {
      ranges[s[i]] = [i];
      uniqueLetters++;
    }
  }

  return [ranges, uniqueLetters];
}

function maxProduct(s) {
  if (s.length === 2) return 1;

  function palChecker(s) {
    let stringInfo = _getStringInfo(s);
    let letterRanges = stringInfo[0];
    let numUniqueLetters = stringInfo[1];

    let bigSubPal = 0;

    for (letter in letterRanges) {
      range = letterRanges[letter];

      left = range[0];
      right = range[range.length - 1];

      if (numUniqueLetters === 1) {
        bigSubPal = range[range.length - 1] - range[0] + 1;
      } else if (left === right) {
        bigSubPal = Math.max(1, bigSubPal);
      } else if (left < right) {
        let substring = s.slice(left + 1, right);
        bigSubPal = Math.max(2 + palChecker(substring), bigSubPal);
      }
    }

    return bigSubPal;
  }
  return palChecker(s);
}

console.log(maxProduct("bb"));
