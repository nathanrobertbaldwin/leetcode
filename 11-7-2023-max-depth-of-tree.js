function maxDepth(root) {
  if (!root) return 0;
  return Math.max(1 + maxDepth(root.left), 1 + maxDepth(root.right));
}
