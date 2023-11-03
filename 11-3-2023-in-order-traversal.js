// 94. Binary Tree Inorder Traversal
// Easy
// Topics
// Companies
// Given the root of a binary tree, return the inorder traversal of its nodes' values.

// Example 1:

// Input: root = [1,null,2,3]
// Output: [1,3,2]
// Example 2:

// Input: root = []
// Output: []
// Example 3:

// Input: root = [1]
// Output: [1]

function inorderTraversal(root) {
  let res = [];
  function traverser(currNode) {
    if (currNode.left) traverser(currNode.left);
    if (currNode.right) traverser(currNode.right);
    res.push(currNode.val);
  }

  traverser(root);
  return res;
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
root.left.left = new Node(3);
root.left.right = new Node(4);
root.right = new Node(5);

console.log(inorderTraversal(root));

// Preorder - Prints value of current node prior to recursive call.
// In order - Traverses to max depth. Once max depth is reached, returns up a level, prints that nodes value, then traverses right.
// Post order - Traverses to max depth. Once max depth is reached, prints that value, returns up a level, then traverses right,
// then prints right value, then returns up a level and prints.
