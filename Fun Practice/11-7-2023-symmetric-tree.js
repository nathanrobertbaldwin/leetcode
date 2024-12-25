// function isSymmetric(root) {
//   let str1 = "";
//   let str2 = "";

//   if (!root.left && !root.right) return true;
//   if (!root.left || !root.right) return false;

//   function LeftPre(node) {
//     if (node.left) LeftPre(node.left);
//     else str1 += "-";
//     if (node.right) LeftPre(node.right);
//     else str1 += "-";
//     str1 += node.val;
//   }

//   function RightPre(node) {
//     if (node.right) RightPre(node.right);
//     else str2 += "-";
//     if (node.left) RightPre(node.left);
//     else str2 += "-";
//     str2 += node.val;
//   }

//   LeftPre(root.left);
//   RightPre(root.right);

//   return str1 === str2;
// }

let symTree = {
  val: 1,
  left: {
    val: 2,
    left: { val: 3, left: null, right: null },
    right: { val: 4, left: null, right: null },
  },
  right: {
    val: 2,
    left: { val: 4, left: null, right: null },
    right: { val: 3, left: null, right: null },
  },
};

let asymTree = {
  val: 1,
  left: { val: 2, left: { val: 2, left: null, right: null }, right: null },
  right: { val: 2, left: { val: 2, left: null, right: null }, right: null },
};

// asymTree:
// inOrder Left of Left Subtree: -2-2-
// inOrder Left of Right Subtree: -2-2-

// inOrder Left of Left Subtree: -2-2-
// InOrder Right of Right Subtree: -2-2-

// preOrder Left of Left Subtree: 22---
// preOrder Left of Right Subtree: 22---

// preOrder Left of Left Subtree: 22---
// preOrder Right of Right Subtre: 2-2--

// postOrder Left of Left Subtree: --2-2
// postOrder Left of Right Subtre: --2-2

// postOrder Left of Left Subtree: --2-2
// postOrder Right of Right Subtree: --2-2

// inorder reads of two different trees can be the same.
// to detect symmetry, do a pre or post order read, but traveling the tree in different directions.

var isSymmetric = function (root) {
  return !root || isSymmetricHelper(root.left, root.right);
};

function isSymmetricHelper(root1, root2) {
  if (!root1 && !root2) return true;
  if (!root1 || !root2) return false;
  return (
    root1.val === root2.val &&
    isSymmetricHelper(root1.left, root2.right) &&
    isSymmetricHelper(root1.right, root2.left)
  );
}

console.log(isSymmetric(asymTree));
