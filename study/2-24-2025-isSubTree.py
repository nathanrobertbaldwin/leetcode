class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Soluiton: This doesn't work! You can't stop the recursion at the point where the subtree ends
# class Solution:
#     def isSubtree(self, root, subRoot) -> bool:
#         if root == None and subRoot == None:
#             return True
#         elif root == None:
#             return False
#         elif subRoot == None:
#             return False
#         elif root.val != subRoot.val:
#             return Solution.isSubtree(self, root.left, subRoot) and Solution.isSubtree(
#                 self, root.right, subRoot
#             )
#         else:
#             return Solution.isSubtree(
#                 self, root.left, subRoot.left
#             ) and Solution.isSubtree(self, root.right, subRoot.right)


# Solution: This doesn't work! We detect a subtree based on val (since the problem doesn't have the same nodes for root and subroot).
# It's possible that we detect treeNode.val == subTreeNode.val high in tree, potentially returning false to early. The actual
# shared subtree could be farther down in the tree, but we won't explore it.


# class Solution:
#     def isSubtree(self, root, subRoot):

#         if subRoot == None:
#             return True
#         if root == None:
#             return False

#         treeStack = [root]

#         while len(treeStack) > 0:
#             treeNode = treeStack.pop()

#             if treeNode != None and treeNode.val == subRoot.val:
#                 subTreeStack = []

#                 treeStack.append(treeNode.right)
#                 treeStack.append(treeNode.left)

#                 subTreeStack.append(subRoot.right)
#                 subTreeStack.append(subRoot.left)

#                 while len(subTreeStack) > 0 and len(treeStack) > 0:
#                     subTreeNode = subTreeStack.pop()
#                     treeNode = treeStack.pop()
#                     if subTreeNode == None and treeNode == None:
#                         continue
#                     elif (
#                         subTreeNode != None
#                         and treeNode != None
#                         and subTreeNode.val != treeNode.val
#                     ):
#                         return False

#                     if treeNode != None:
#                         treeStack.append(treeNode.right)
#                         treeStack.append(treeNode.left)
#                     if subTreeNode != None:
#                         subTreeStack.append(subTreeNode.right)
#                         subTreeStack.append(subTreeNode.left)

#             if treeNode != None:
#                 treeStack.append(treeNode.right)
#                 treeStack.append(treeNode.left)

#         return True


root = [1, 2, 3, 4, 5]
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
# root.left.left.left = TreeNode(6)

# subRoot = [2, 4, 5]
subRoot = TreeNode(2)
subRoot.left = TreeNode(4)
subRoot.right = TreeNode(5)

print(Solution.isSubtree(None, root, subRoot))  # false

root = TreeNode(1)
subRoot = TreeNode(0)
print(Solution.isSubtree(None, root, subRoot))  # false
