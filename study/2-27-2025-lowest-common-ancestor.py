# Lowest Common Ancestor in Binary Search Tree
# Solved

# Given a binary search tree (BST) where all node values are unique, and two nodes from the tree p and q, return the lowest common ancestor (LCA) of the two nodes.

# The lowest common ancestor between two nodes p and q is the lowest node in a tree T such that both p and q as descendants. The ancestor is allowed to be a descendant of itself.


class Solution:
    def lowestCommonAncestor(self, root, p, q):
        if root == None:
            return
        elif root.val == p.val or root.val == q.val:
            return root
        elif (p.val < root.val and q.val > root.val) or (
            p.val > root.val and q.val < root.val
        ):
            return root
        else:
            if p.val < root.val and q.val < root.val:
                return Solution.lowestCommonAncestor(self, root.left, p, q)
            elif p.val > root.val and q.val > root.val:
                return Solution.lowestCommonAncestor(self, root.right, p, q)


class Solution:
    def lowestCommonAncestor(self, root, p, q):
        cur = root

        while cur:
            if p.val > cur.val and q.val > cur.val:
                cur = cur.right
            elif p.val < cur.val and q.val < cur.val:
                cur = cur.left
            else:
                return cur
