// You are given a 0-indexed sorted array of integers nums.

// You can perform the following operation any number of times:

//     Choose two indices, i and j, where i < j, such that nums[i] < nums[j].
//     Then, remove the elements at indices i and j from nums. The remaining elements retain their original order, and the array is re-indexed.

// Return an integer that denotes the minimum length of nums after performing the operation any number of times (including zero).

// Note that nums is sorted in non-decreasing order.

// Example 1:

// Input: nums = [1,3,4,9]
// Output: 0
// Explanation: Initially, nums = [1, 3, 4, 9].
// In the first operation, we can choose index 0 and 1 because nums[0] < nums[1] <=> 1 < 3.
// Remove indices 0 and 1, and nums becomes [4, 9].
// For the next operation, we can choose index 0 and 1 because nums[0] < nums[1] <=> 4 < 9.
// Remove indices 0 and 1, and nums becomes an empty array [].
// Hence, the minimum length achievable is 0.

// function minLengthAfterRemovals(nums) {
//   let rems = [];

//   for (let i = 0; i < nums.length; i++) {
//     if (nums[i] > nums[i + 1]) {
//       rems.push(nums[i]);
//     }
//   }
//   if (rems.length > 0) {
//   }
//   return rems;
// }

// how to deal with odd nums length

// arr = [8, 3, 5]

function minLengthAfterRemovals(a) {
  let n = a.length;

  let count = 0;
  let half = Math.trunc(n / 2);
  for (let i = 0, j = half; i < half && j < n; ) {
    let L = a[i]; // left = start to mid
    let R = a[j]; // right = mid to end

    if (L < R) {
      i++;
      j++;
      count += 2; // two elements matched - to be removed
    } else {
      j++;
    }
  }
  return n - count; // remaining elements
}

let arr = [1, 3, 4, 9];

console.log(minLengthAfterRemovals(arr));
