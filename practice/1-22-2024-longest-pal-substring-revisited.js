function longestPalindrome(s) {
  let palLengths = new Array(s.length).fill(0);

  for (let i = 0; i < s.length; i++) {
    d = 0;
    while (i - d >= 0 && i + d < s.length) {
      if (s[i - d] === s[i + d]) {
        palLengths[i - d] = d * 2 + 1;
        d++;
      } else break;
    }

    d = 0;
    if (s[i] === s[i + 1]) {
      while (i - d >= 0 && i + d + 1 < s.length) {
        if (s[i - d] === s[i + d + 1]) {
          palLengths[i - d] = d * 2 + 2;
          d++;
        } else break;
      }
    }
  }

  let maxLength = 0;
  let indexOfMax = 0;
  for (let i = 0; i < palLengths.length; i++) {
    if (maxLength <= palLengths[i]) {
      maxLength = palLengths[i];
      indexOfMax = i;
    }
  }

  //   console.log(palLengths);
  return s.slice(indexOfMax, indexOfMax + maxLength);
}

console.log(longestPalindrome("ccx"));
