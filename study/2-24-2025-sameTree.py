class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Solution: Standard recursive traversal of the tree
# Time Complexity: O(n)
# Space Complexity: Depends on the shape of the tree:
# If the tree is balanced, space complexity is O(log(n))
# If the tree has degenerated to a linked list, space complexity is O(n)

# class Solution:
#     def isSameTree(self, p, q):
#         if p == None and q == None:
#             return True
#         if p == None:
#             return False
#         if q == None:
#             return False
#         if p.val != q.val:
#             return False

#         return Solution.isSameTree(self, p.left, q.left) and Solution.isSameTree(
#             self, p.right, q.right
#         )


class Solution:
    def isSameTree(self, p, q):
        p_stack = [p]
        q_stack = [q]

        while len(p_stack) > 0 and len(q_stack) > 0:
            curr_p = p_stack.pop()
            curr_q = q_stack.pop()

            if curr_p == None and curr_q == None:
                continue

            elif curr_p == None:
                return False

            elif curr_q == None:
                return False

            elif curr_p.val != curr_q.val:
                return False

            else:
                p_stack.append(curr_p.left)
                p_stack.append(curr_p.right)
                q_stack.append(curr_q.left)
                q_stack.append(curr_q.right)

        if len(p_stack) != len(q_stack):
            return False

        return True


# p = [1, 2, 3]
# q = [1, 2, 3]

p_root = TreeNode(1)
p_root.left = TreeNode(2)
p_root.right = TreeNode(3)

q_root = TreeNode(1)
q_root.left = TreeNode(2)
q_root.right = TreeNode(3)

print(Solution.isSameTree(None, p_root, q_root))
