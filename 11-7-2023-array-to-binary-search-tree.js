// 108. Convert Sorted Array to Binary Search Tree
// Easy
// Topics
// Companies
// Given an integer array nums where the elements are sorted in ascending order, convert it to a
// height-balanced
//  binary search tree.

// Example 1:

// Input: nums = [-10,-3,0,5,9]
// Output: [0,-3,9,-10,null,5]
// Explanation: [0,-10,5,null,-3,null,9] is also accepted:

// Example 2:

// Input: nums = [1,3]
// Output: [3,1]
// Explanation: [1,null,3] and [3,1] are both height-balanced BSTs.

let array1 = [1, 2, 3, 4];

function sortedArrayToBST(arr) {
  if (arr.length === 1) return { val: arr[0], left: null, right: null };
  if (arr.length === 0) return null;

  let mid = Math.floor(arr.length / 2);
  
  return {
    val: arr[mid],
    left: sortedArrayToBST(arr.slice(0, mid)),
    right: sortedArrayToBST(arr.slice(mid + 1)),
  };
}

console.log(sortedArrayToBST(array1));
