def lowestCommonAncestor(root, p, q):
    if root == None or root == p or root == q:
        return root

    left = lowestCommonAncestor(root.left, p, q)
    right = lowestCommonAncestor(root.right, p, q)

    if left and right:
        return root.val

    return left if left else right


class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


root = Node(1)

root.left = Node(2)
root.right = Node(3)

root.left.left = Node(4)
root.left.right = Node(5)

root.right.left = Node(6)
root.right.right = Node(7)

print(lowestCommonAncestor(root, root.left.left, root.left.right))
