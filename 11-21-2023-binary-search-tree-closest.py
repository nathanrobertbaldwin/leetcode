def closestValue(root, target: float) -> int:
    if root.left != None and abs(root.left.val - target) < abs(root.val - target):
        return closestValue(root.left, target)
    elif root.right != None and abs(root.right.val - target) < abs(root.val - target):
        return closestValue(root.right, target)
    else:
        return root.val


class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


root = Node(4)
root.left = Node(2)
root.right = Node(5)
root.left.left = Node(1)
root.left.right = Node(3)

print(closestValue(root, 3.714286))
