var inorderTraversal = function (root) {
  //left_subtree Root right_subtree
  return dfs(root, []);
};
var dfs = function (root, result) {
  if (root == null) {
    return result;
  }
  dfs(root.left, result);
  result.push(root.val);
  dfs(root.right, result);
  return result;
};

let binTree = {
  left: null,
  right: {
    left: null,
    right: {
      left: null,
      right: null,
      val: 3,
    },
    val: 2,
  },
  val: 1,
};

console.log(inorderTraversal(binTree));
