def evaluateTree(root):
    def evaluate(root):
        if root == Null:
            return
        if root.val == 0:
            return False
        if root.val == 1:
            return True
        if root.val == 2:
            return evaluate(root.left) or evaluate(root.right)
        if root.val == 3:
            return evaluate(root.left) and evaluate(root.right)

    return evaluate(root)
