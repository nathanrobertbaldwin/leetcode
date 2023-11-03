// /**
//  * Definition for a binary tree node.
//  * function TreeNode(val, left, right) {
//  *     this.val = (val===undefined ? 0 : val)
//  *     this.left = (left===undefined ? null : left)
//  *     this.right = (right===undefined ? null : right)
//  * }
//  */
// /**
//  * @param {TreeNode} p
//  * @param {TreeNode} q
//  * @return {boolean}
//  */

// Check initial values, return false if different.
//

function inorderTraversal(root) {
  let res = [];
  if (root === null) return res;

  function traverser(currNode) {
    if (currNode.left) traverser(currNode.left);
    if (currNode.val !== null) res.push(currNode.val);
    if (currNode.right) traverser(currNode.right);
  }

  traverser(root);
  return res;
}

var isSameTree = function (p, q) {
  let pString = inorderTraversal(p).toString();
  let qString = inorderTraversal(q).toString();
  return pString === qString;
};

class Node {
  constructor(value) {
    this.val = value;
    this.left = null;
    this.right = null;
  }
}

rootP = new Node(1);
rootP.right = new Node(1);

rootQ = new Node(1);
rootQ.left = new Node(null);
rootQ.right = new Node(1);

console.log(isSameTree(rootP, rootQ));
