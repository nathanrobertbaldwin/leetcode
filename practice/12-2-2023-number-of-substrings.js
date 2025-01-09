function countCompleteSubstrings(word, k) {
  function isValid(word) {
    let alpha = {
      a: 0,
      b: 1,
      c: 2,
      d: 3,
      e: 4,
      f: 5,
      g: 6,
      h: 7,
      i: 8,
      j: 9,
      k: 10,
      l: 11,
      m: 12,
      n: 13,
      o: 14,
      p: 15,
      q: 16,
      r: 17,
      s: 18,
      t: 19,
      u: 20,
      v: 21,
      w: 22,
      x: 23,
      y: 24,
      z: 25,
    };

    for (let i = 0; i < word.length - 1; i++) {
      if (Math.abs(alpha[word[i]] - alpha[word[i + 1]]) > 2) return false;
    }
    return true;
  }

  let validCount = 0;

  function subStringCounter(word, k) {
    divs = Math.floor(word / k);
    remainder = word % k;
    sect = 0;

    while ()
    while ((divNumber + 1) * k < word.length) {
      if (isValid(word.slice(sect * k, (sect + 1) * k + 1))) count += 1;
      sect++;
    }
  }
}
