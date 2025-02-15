# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:

        left = head
        middle = head.next
        left.next = None

        while middle:
            right = middle.next
            middle.next = left
            left = middle
            middle = right

        return left

    def printList(self, head):
        while head:
            print(head.val)
            head = head.next


head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)

print(Solution.printList(None, Solution.reverseList(None, head)))
