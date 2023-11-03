// Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).

// Example 1:

// Input: root = [1,2,2,3,4,4,3]
// Output: true

function isSymmetric(root) {
  return isSymmetric(root.left) === isSymmetric(root.right);
}

class Node {
  constructor(value) {
    this.val = value;
    this.left = null;
    this.right = null;
  }
}

root = new Node(1);
root.left = new Node(2);
root.right = new Node(2);
root.left.right = new Node(4);
root.right = new Node(5);
