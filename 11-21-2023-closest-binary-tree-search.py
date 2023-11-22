def closestValue(self, root: Optional[TreeNode], target: float) -> int:
    def binSearch(node, target, closest):
        if node == None:
            return closest

        if node.val == target:
            return node.val

        if abs(target - node.val) <= abs(target - closest):
            if abs(target - node.val) == abs(target - closest):
                closest = min(node.val, closest)
            else:
                closest = node.val
        if target < node.val:
            return binSearch(node.left, target, closest)
        elif target > node.val:
            return binSearch(node.right, target, closest)

    return binSearch(root, target, root.val)
