function maxProduct(s) {
  let largest = 1;
  let secondLargest = 1;

  function getStringInfo(s) {
    let ranges = {};
    let length = 0;

    for (let i = 0; i < s.length; i++) {
      if (s[i] in ranges) {
        if (ranges[s[i]].length === 1) {
          ranges[s[i]].push(i);
        } else {
          ranges[s[i]][1] = i;
        }
      } else {
        ranges[s[i]] = [i];
        length++;
      }
    }

    return [ranges, length];
  }

  function subStringChecker(s) {
    let stringInfo = getStringInfo(s);
    let letterRanges = stringInfo[0];
    let numUniqueLetters = stringInfo[1];

    if (numUniqueLetters === 1) {
      for (letter in letterRanges) {
        range = letterRanges[letter];
        return range[range.length - 1] - range[0] + 1;
      }
    } else {
      let maxSubPalLength = 0;
      for (letter in letterRanges) {
        range = letterRanges[letter];
        if (range.length === 1) maxSubPalLength = Math.max(maxSubPalLength, 1);
        else {
          left = range[0] + 1;
          right = range[1];
          if (left === right) maxSubPalLength = Math.max(maxSubPalLength, 2);
          else {
            maxSubPalLength = Math.max(
              2 + subStringChecker(s.slice(left, right)),
              maxSubPalLength
            );
          }
        }
      }
      if (maxSubPalLength > secondLargest) secondLargest = maxSubPalLength;
      if (maxSubPalLength > largest) {
        secondLargest = largest;
        largest = maxSubPalLength;
      }
    }
  }
  subStringChecker(s);
  return [largest, secondLargest];
}

console.log(maxProduct("accbcaxxcxx"));
