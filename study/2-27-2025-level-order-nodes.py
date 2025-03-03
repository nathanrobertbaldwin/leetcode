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


class Solution:
    def levelOrder(self, root):

        if root == None:
            return []

        currentLevelQueue = [root]
        nodes = []

        while True:
            currentLevelNodes = []
            nextLevelQueue = []

            while len(currentLevelQueue) > 0:
                currentNode = currentLevelQueue.pop(0)
                if currentNode.left != None:
                    nextLevelQueue.append(currentNode.left)
                if currentNode.right != None:
                    nextLevelQueue.append(currentNode.right)
                currentLevelNodes.append(currentNode.val)
            nodes.append(currentLevelNodes)

            currentLevelQueue = nextLevelQueue
            if len(currentLevelQueue) == 0:
                break

        return nodes


# empty list
root = None
print(Solution.levelOrder(None, root))  # []

# linked list
root = TreeNode(1)
root.left = TreeNode(2)
root.left.left = TreeNode(3)
root.left.left.left = TreeNode(4)
root.left.left.left.left = TreeNode(5)
print(Solution.levelOrder(None, root))  # [[1], [2], [3], [4], [5]]

# balanced tree
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)
print(Solution.levelOrder(None, root))  #  [[1],[2,3],[4,5,6,7]]

# imbalanced tree
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = None
root.right.left = None
root.right.right = TreeNode(7)
print(Solution.levelOrder(None, root))  #  [[1],[2,3],[4,7]]
