class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rightSideView(self, root):
        nodes = []

        def dfs(self, root):

            nonlocal nodes

            if root == None:
                return

            nodes.append(root.val)
            dfs(self, root.right)

        dfs(None, root)
        return nodes


# empty list
root = None
print(Solution.rightSideView(None, root))  # []

# linked list
root = TreeNode(1)
root.left = TreeNode(2)
root.left.left = TreeNode(3)
root.left.left.left = TreeNode(4)
root.left.left.left.left = TreeNode(5)
print(Solution.rightSideView(None, root))  # [1]

# balanced tree
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)
print(Solution.rightSideView(None, root))  #  [1, 3, 7]

# imbalanced tree
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = None
print(Solution.rightSideView(None, root))  #  [1, 3]
