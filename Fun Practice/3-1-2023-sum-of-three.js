// Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

// Notice that the solution set must not contain duplicate triplets.

// Example 1:

// Input: nums = [-1,0,1,2,-1,-4]
// Output: [[-1,-1,2],[-1,0,1]]
// Explanation:
// nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
// nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
// nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
// The distinct triplets are [-1,0,1] and [-1,-1,2].
// Notice that the order of the output and the order of the triplets does not matter.
// Example 2:

// Input: nums = [0,1,1]
// Output: []
// Explanation: The only possible triplet does not sum up to 0.
// Example 3:

// Input: nums = [0,0,0]
// Output: [[0,0,0]]
// Explanation: The only possible triplet sums up to 0.

// Notes: 1. input is uns array of nums.
// 2. output is an array of triplets.
// 3. Each element of triplet must be different index from input.
// 4. Triplets sum to 0.

// pseudocode:
// 1. Sort.
// 3. Pointer at left of s array, pointer at right.
// 4. Take sum.
// 6. If t for bin search is less than left pointer plus one, move left pointer in.
// 7. If t for bin search is greater than right pointer minus one, move right pointer in.
// 5. Set as t for bin search.
// 8. else bin search for t.
// 9. If bin search returns idx for t, add to result.
// 10. Also check right and left of idx?

function pivotSort(arr) {
  if (arr.length <= 1) return arr;

  let pivot = arr[0];
  let less = [];
  let more = [];

  for (let i = 1; i < arr.length; i++) {
    if (arr[i] <= pivot) less.push(arr[i]);
    else more.push(arr[i]);
  }

  return [...pivotSort(less), pivot, ...pivotSort(more)];
}

function binSearchSlice(arr, l_bound, r_bound, target) {
  let l_idx = l_bound + 1;
  let r_idx = r_bound - 1;
  let m_idx = Math.floor((l_idx + r_idx) / 2);

  while (l_idx <= r_idx) {
    if (target < arr[m_idx]) {
      r_idx = m_idx - 1;
      m_idx = Math.floor((r_idx + l_idx) / 2);
    } else if (target > arr[m_idx]) {
      l_idx = m_idx + 1;
      m_idx = Math.floor((r_idx + l_idx) / 2);
    } else {
      return m_idx;
    }
  }
  return -1;
}

function threeSum(arr) {
  let res = [];
  let exists = new Set();

  let sort = pivotSort(arr);

  let l_bound = 0;
  let r_bound = sort.length - 1;

  while (r_bound - l_bound > 1) {
    for (let r_idx = r_bound; r_idx > l_bound; r_idx--) {
      let target = -1 * (sort[l_bound] + sort[r_idx]);

      if (target > sort[r_idx - 1]) break;

      let target_idx = binSearchSlice(sort, l_bound, r_idx, target);

      if (target_idx > -1) {
        let combo = [sort[l_bound], sort[target_idx], sort[r_idx]];
        if (!exists.has(combo.toString())) {
          res.push(combo);
          exists.add(combo.toString());
        }
      }
    }
    l_bound++;
  }

  return res;
}

// Input: nums = [-1,0,1,2,-1,-4]
// Output: [[-1,-1,2],[-1,0,1]]

console.log(threeSum([-1, 0, 1, 2, -1, -4]));
