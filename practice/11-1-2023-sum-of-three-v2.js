function mergeArrs(arr1, arr2) {
  let res = [];
  let i = 0;
  let j = 0;

  while (i < arr1.length || j < arr2.length) {
    if (i === arr1.length) {
      res.push(arr2[j]);
      j++;
      continue;
    } else if (j === arr2.length) {
      res.push(arr1[i]);
      i++;
      continue;
    }

    if (arr1[i] < arr2[j]) {
      res.push(arr1[i]);
      i++;
      continue;
    } else {
      res.push(arr2[j]);
      j++;
      continue;
    }
  }
  return res;
}

function mergeSort(arr) {
  if (arr.length <= 1) return arr;
  let mid = Math.floor(arr.length / 2);
  return [
    ...mergeArrs(mergeSort(arr.slice(0, mid)), mergeSort(arr.slice(mid))),
  ];
}

// function threeSum(arr) {
//   let sorted = mergeSort(arr);
//   let res = [];

//   let l_bound = 0;
//   let r_bound = sorted.length - 1;

//   while (r_bound - l_bound > 1) {
//     if (sorted[l_bound] > 0) break;
//     if (sorted[]) l_bound++;

//     let left = l_bound + 1;
//     let right = r_bound;

//     while (left < right) {
//       let sum = sorted[l_bound] + sorted[left] + sorted[right];
//       if (sum < 0) left++;
//       else if (sum > 0) right--;
//       else {
//         res.push([sorted[l_bound], sorted[left], sorted[right]]);
//         break;
//       }
//     }

//     l_bound++;
//   }

//   return res;
// }

var threeSum = function (array) {
  array.sort((a, b) => a - b);
  const triplets = [];

  for (let i = 0; i < array.length - 2; i++) {
    if (array[i] != array[i - 1]) {
      // making sure our solution set does not contain duplicate triplets
      let left = i + 1;
      let right = array.length - 1;

      while (left < right) {
        const currentSum = array[i] + array[left] + array[right];
        if (currentSum === 0) {
          triplets.push([array[i], array[left], array[right]]);
          while (array[left] == array[left + 1]) left++;
          while (array[right] == array[right - 1]) right--; // making sure our solution set does not contain duplicate triplets
          left++;
          right--;
        } else if (currentSum < 0) {
          left++;
        } else if (currentSum > 0) {
          right--;
        }
      }
    }
  }
  return triplets;
};

console.log(threeSum([0, 0, 0, 0]));
