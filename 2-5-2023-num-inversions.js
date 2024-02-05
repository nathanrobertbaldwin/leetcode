function mergeSort(arr) {
  if (arr.length <= 1) {
    return [arr, 0];
  }

  // Split the array into two halves
  const m = Math.floor(arr.length / 2);
  const l = arr.slice(0, m);
  const r = arr.slice(m);

  // Recursively apply mergeSort to the two halves
  const [lSorted, lCount] = mergeSort(l);
  const [rSorted, rCount] = mergeSort(r);
  const [merged, currCount] = merge(lSorted, rSorted);
  // Merge the sorted halves
  console.log([merged, lCount + rCount + currCount]);
  return [merged, lCount + rCount + currCount];
}

function merge(left, right) {
  let res = [];
  let lidx = 0;
  let ridx = 0;
  let currCount = 0;
  // Compare elements from both arrays and merge them
  while (lidx < left.length && ridx < right.length) {
    if (left[lidx] < right[ridx]) {
      res.push(left[lidx]);
      lidx++;
      currCount += ridx;
    } else {
      res.push(right[ridx]);
      ridx++;
    }
  }

  while (lidx < left.length) {
    res.push(left[lidx]);
    lidx++;
    currCount += ridx;
  }

  while (ridx < right.length) {
    res.push(right[ridx]);
    ridx++;
  }

  // Add remaining elements from both arrays (if any)
  return [res, currCount];
}

console.log(mergeSort([4, 1, 5, 6, 3, 2]));
