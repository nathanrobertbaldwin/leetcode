function merge(arr1, arr2) {
  let mergedArrs = [];
  let i = 0;
  let j = 0;
  while (i < arr1.length || j < arr2.length) {
    if (i === arr1.length) {
      mergedArrs.push(arr2[j]);
      j++;
    } else if (j === arr2.length) {
      mergedArrs.push(arr1[i]);
      i++;
    } else if (arr1[i] <= arr2[j]) {
      mergedArrs.push(arr1[i]);
      i++;
    } else {
      mergedArrs.push(arr2[j]);
      j++;
    }
  }
  return mergedArrs;
}

function sortSuffixArr(arr) {
  if (arr.length <= 1) {
    return arr;
  } else {
    let mid = Math.floor(arr.length / 2);
    return merge(
      sortSuffixArr(arr.slice(0, mid)),
      sortSuffixArr(arr.slice(mid))
    );
  }
}

function suffixSort(str, k) {
  let suffixes = [];

  for (let i = 0; i < str.length; i++) {
    suffixes.push(str.slice(i, str.length));
  }

  let sortedSuffixes = sortSuffixArr(suffixes);

  return sortedSuffixes;
}

console.log(suffixSort("aasdgergaseg", 3));
