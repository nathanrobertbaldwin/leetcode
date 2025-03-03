# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        countGood = 0

        def dfs(self, root, maxRoot):
            nonlocal countGood

            if root == None:
                return

            if root.val >= maxRoot:
                countGood += 1

            maxRoot = max(maxRoot, root.val)

            dfs(self, root.left, maxRoot)
            # below is wrong: If you see a larger val higher up in the tree, we don't replace it with the current node val.
            # maxRoot = root.val
            dfs(self, root.right, maxRoot)

        dfs(self, root, -101)
        return countGood


# # empty list
# root = None
# print(Solution.goodNodes(None, root))  # []

# # linked list
# root = TreeNode(1)
# root.left = TreeNode(2)
# root.left.left = TreeNode(3)
# root.left.left.left = TreeNode(4)
# root.left.left.left.left = TreeNode(5)
# print(Solution.goodNodes(None, root))  # 5

# # balanced tree
# root = TreeNode(1)
# root.left = TreeNode(2)
# root.right = TreeNode(8)
# root.left.left = TreeNode(4)
# root.left.right = TreeNode(5)
# root.right.left = TreeNode(6)
# root.right.right = TreeNode(7)
# print(Solution.goodNodes(None, root))  #  5

# root = [5, 3, 4, null, 3, null, 5, 5]

root = TreeNode(5)
root.left = TreeNode(3)
root.left.left = None
root.left.right = TreeNode(3)
root.right = TreeNode(4)
root.right.left = None
root.right.right = TreeNode(5)
root.left.right.left = TreeNode(5)


print(Solution.goodNodes(None, root))  #  4
