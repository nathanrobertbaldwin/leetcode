# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def height(root):
    global nodesTraversed
    if root == None:
        return -1

    print("Visiting node:", root.val)
    left_height = 1 + height(root.left)
    right_height = 1 + height(root.right)

    return max(left_height, right_height)


# Brute force:
# Each node needs to test whether the sum of the heights of its left and right subtrees
# is greater than the current diameter
# Then this node will call check diameter on its right and left subtrees.
def diameterOfBinaryTree(root):
    global nodesTraversed
    if root == None:
        return 0

    print("Visiting node:", root.val)
    left_height = 1 + height(root.left)
    right_height = 1 + height(root.right)
    this_nodes_diameter = left_height + right_height
    max_sub_tree_diameter = max(
        diameterOfBinaryTree(root.left), diameterOfBinaryTree(root.right)
    )
    return max(this_nodes_diameter, max_sub_tree_diameter)


def diameterOfBinaryTree(root):
    res = 0

    def dfs(root):
        nonlocal res

        if root == None:
            return 0

        left = dfs(root.left)
        right = dfs(root.right)
        res = max(res, left + right)

        return 1 + max(left, right)

    dfs(root)
    return res


# root = TreeNode(1)
# root.right = TreeNode(2)
# root.right.left = TreeNode(3)
# root.right.left.left = TreeNode(5)
# root.right.right = TreeNode(4)

# 2^n - 1 nodes in a full tree
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)

print(diameterOfBinaryTree(root))
