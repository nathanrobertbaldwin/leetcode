// Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).

// Example 1:

// Input: root = [1,2,2,3,4,4,3]
// Output: true

function isSymmetric(root) {
  function splitTrees(p, q) {
    if (p === null && q === null) return true;
    if (p === null || q === null || p.val !== q.val) return false;
    return splitTrees(p.left, q.right) && splitTrees(p.right, q.left);
  }
  return splitTrees(root.left, root.right);
}

class Node {
  constructor(value) {
    this.val = value;
    this.left = null;
    this.right = null;
  }
}

rootP = new Node(1);
rootP.left = new Node(2);
rootP.left.left = new Node(3);
rootP.left.right = new Node(4);
rootP.right = new Node(2);
rootP.right.left = new Node(4);
rootP.right.right = new Node(2);

console.log(isSymmetric(rootP));
