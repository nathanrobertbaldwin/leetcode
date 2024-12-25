function pivotSort(arr) {
  if (arr.length <= 1) return arr;
  let pivot = arr[0];
  let more = [];
  let less = [];
  for (let i = 1; i < arr.length; i++) {
    if (arr[i] < pivot) less.push(arr[i]);
    else more.push(arr[i]);
  }
  return [...pivotSort(less), pivot, ...pivotSort(more)];
}

function threeSum(arr) {
  let sorted = pivotSort(arr);
  let res = [];

  for (let l_bound = 0; l_bound < sorted.length - 2; l_bound++) {
    if (sorted[l_bound] > 0) break;
    let left = l_bound + 1;
    let right = arr.length - 1;
    while (left < right) {
      let currentSum = sorted[l_bound] + sorted[left] + sorted[right];
      if (currentSum === 0) {
        res.push([sorted[l_bound], sorted[left], sorted[right]]);
        while (sorted[left] === sorted[left + 1]) left++;
        while (sorted[right] === sorted[right - 1]) right--;
        left++;
        right--;
      } else if (currentSum < 0) {
        left++;
      } else if (currentSum > 0) {
        right--;
      }
    }
    while (sorted[l_bound] === sorted[l_bound + 1]) l_bound++;
  }
  return res;
}

console.log(typeof 1);

console.log(threeSum([-4, -1, -1, 0, 1, 2]));
