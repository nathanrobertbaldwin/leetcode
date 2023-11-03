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
    if (!currNode.left) res.push(" ");
    else traverser(currNode.left);
    res.push(currNode.val);
    if (!currNode.right) res.push(" ");
    else traverser(currNode.right);
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

let rootP = new Node(1);
rootP.right = new Node(2);

let rootQ = new Node(1);
rootQ.left = new Node(2);

function isSameTreeV2(p, q) {
  if (p === null && q === null) return true;
  if (p === null || q === null || p.val !== q.val) return false;
  return isSameTreeV2(p.left, q.left) && isSameTree(p.right, q.right);
}

console.log(isSameTreeV2(rootP, rootQ));
