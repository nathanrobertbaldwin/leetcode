function findMax(arr) {
  max = -Infinity;
  for (i = 0; i < arr.length; i++) {
    if (arr[i] > max) max = arr[i];
  }
  return max;
}

steelbrick
