# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root):

        if root == None:
            return []

        q = [root]

        nodes = []
        maxNodes = 1
        nodeCount = 0

        levelNodes = []
        while len(q) > 0:
            currentNode = q.pop(0)
            nodeCount += 1
            if currentNode != None:
                levelNodes.append(currentNode.val)
                if currentNode.left != None:
                    q.append(currentNode.left)
                if currentNode.right != None:
                    q.append(currentNode.right)
            if nodeCount == maxNodes or len(q) == 0:
                nodeCount = 0
                nodes.append(levelNodes)
                levelNodes = []
                maxNodes *= 2

        return nodes


root = TreeNode(1)
root.left = TreeNode(2)
root.left.left = TreeNode(3)
root.left.left.left = TreeNode(4)
root.left.left.left.left = TreeNode(5)


print(Solution.levelOrder(None, root))
