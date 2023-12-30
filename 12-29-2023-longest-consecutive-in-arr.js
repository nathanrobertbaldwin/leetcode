function merge(a1, a2) {
  let merged = [];
  let i = 0;
  let j = 0;
  while (i < a1.length || j < a2.length) {
    if (a1[i] <= a2[j]) {
      merged.push(a1[i]);
      i++;
    } else if (a2[j] < a1[i]) {
      merged.push(a2[j]);
      j++;
    } else if (i === a1.length) {
      merged.push(a2[j]);
      j++;
    } else if (j === a2.length) {
      merged.push(a1[i]);
      i++;
    }
  }
  return merged;
}

function sortArr(a) {
  if (a.length <= 1) {
    return a;
  } else {
    let mid = Math.floor(a.length / 2);
    let firstHalf = a.slice(0, mid);
    let secondHalf = a.slice(mid, a.length);
    return merge(sortArr(firstHalf), sortArr(secondHalf));
  }
}

function longestConsecutiveSequence(a) {
  a = sortArr(a);

  let maxSequenceLength = 0;
  let sequenceLength = 1;

  for (let i = 0; i < a.length - 1; i++) {
    if (a[i] + 1 === a[i + 1]) {
      sequenceLength++;
    } else {
      if (sequenceLength > maxSequenceLength) {
        maxSequenceLength = sequenceLength;
        sequenceLength = 1;
      }
    }
  }

  if (sequenceLength > maxSequenceLength) {
    maxSequenceLength = sequenceLength;
  }

  return maxSequenceLength;
}

console.log(longestConsecutiveSequence([0, 3, 7, 2, 5, 8, 4, 6, 0, 1]));
