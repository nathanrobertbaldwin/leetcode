function binTreeMaxDepth(node) {
  if (node == Null) return -1;
  else {
    return Math.max(
      1 + binTreeMaxDepth(node.left),
      1 + binTreeMaxDepth(node.right)
    );
  }
}

