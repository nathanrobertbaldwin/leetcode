class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head, n: int):

        listSize = 0
        currentNode = head
        while currentNode != None:
            listSize += 1
            currentNode = currentNode.next

        targetNode = listSize - n

        if targetNode == 0:
            return head.next

        previousNode = None
        currentNode = head
        while targetNode > 0:
            previousNode = currentNode
            currentNode = currentNode.next
            targetNode -= 1

        previousNode.next = currentNode.next
        return head


# nodes = [1, 2, 3, 4]
# n = 1  # [1,2,4]

# nodes = [5]
# n = 1  # []

# nodes = [1, 2]
# n = 2  # [2]

currentNode = head = ListNode(nodes[0])
for i in range(1, len(nodes)):
    currentNode.next = ListNode(nodes[i])
    currentNode = currentNode.next

currentNode = Solution.removeNthFromEnd(None, head, n)
while currentNode != None:
    print(currentNode.val)
    currentNode = currentNode.next
