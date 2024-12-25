// 112. Path Sum
// Easy
// Topics
// Companies
// Given the root of a binary tree and an integer targetSum, return true if the tree has a root-to-leaf path such that adding up all the values along the path equals targetSum.

// A leaf is a node with no children.

function hasPathSum(root, targetSum) {
  let ans = false;
  if (root === null) return ans;

  function pathing(node, targetSum) {
    if (node.val === targetSum && node.left === null && node.right === null) {
      ans = true;
      return;
    }
    if (node.left !== null) pathing(node.left, targetSum - node.val);
    if (node.right !== null) pathing(node.right, targetSum - node.val);
  }

  pathing(root, targetSum);
  return ans;
}

let rootA = {
  val: 5,
  left: {
    val: 4,
    left: {
      val: 11,
      left: { val: 7, left: null, right: null },
      right: { val: 2, left: null, right: null },
    },
    right: null,
  },
  right: {
    val: 8,
    left: { val: 13, left: null, right: null },
    right: { val: 4, left: null, right: { val: 1, left: null, right: null } },
  },
};

let rootB = {
  val: -2,
  left: null,
  right: { val: -3, left: null, right: null },
};

console.log(hasPathSum(rootB, -5));
