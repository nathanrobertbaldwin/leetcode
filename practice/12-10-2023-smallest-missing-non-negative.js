// 2598. Smallest Missing Non-negative Integer After Operations
// Medium
// Topics
// Companies
// Hint

// You are given a 0-indexed integer array nums and an integer value.

// In one operation, you can add or subtract value from any element of nums.

//     For example, if nums = [1,2,3] and value = 2, you can choose to subtract value from nums[0] to make nums = [-1,2,3].

// The MEX (minimum excluded) of an array is the smallest missing non-negative integer in it.

//     For example, the MEX of [-1,2,3] is 0 while the MEX of [1,0,3] is 2.

// Return the maximum MEX of nums after applying the mentioned operation any number of times.

// Example 1:

// Input: nums = [1,-10,7,13,6,8], value = 5
// Output: 4
// Explanation: One can achieve this result by applying the following operations:
// - Add value to nums[1] twice to make nums = [1,0,7,13,6,8]
// - Subtract value from nums[2] once to make nums = [1,0,2,13,6,8]
// - Subtract value from nums[3] twice to make nums = [1,0,2,3,6,8]
// The MEX of nums is 4. It can be shown that 4 is the maximum MEX we can achieve.

// Brute Force:
// loop through array mutating each element until it's positive and as close to zero as possible
// Use a second array to track which elements you have by inserting val at the same index
// First empty index is answer

function findSmallestInteger(nums, value) {
  res = new Array(nums.length).fill(false);

  for (let i = 0; i < nums.length; i++) {
    if (value === 0 && nums[i] > 0) res[nums[i]] = true;
    else if (nums[i] >= 0) res[nums[i] % value] = true;
    else if (nums[i] < 0) {
      remainder = nums[i] % value;
      if (remainder === 0) res[0] = true;
      else res[Math.abs(remainder) + (nums[i] % value)] = true;
    }
    console.log(res);
  }

  for (let i = 0; i < res.length; i++) {
    if (res[i] === false) return i;
  }
}

// nums =
// [3,0,3,2,4,2,1,1,0,4]
// value =
// 5

console.log(findSmallestInteger([3, 0, 3, 2, 4, 2, 1, 1, 0, 4], 5));
