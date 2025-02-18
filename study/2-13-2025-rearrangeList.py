# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reorderList(self, head) -> None:

        if head == None:
            return None

        currentNode = head.next
        listLength = 1
        while currentNode != None:
            currentNode = currentNode.next
            listLength += 1

        queue = []
        stack = []

        currentNode = head.next
        count = 1
        while currentNode != None:
            if listLength % 2 == 0:
                if count < listLength // 2:
                    queue.append(currentNode)
                else:
                    stack.append(currentNode)
            else:
                if count <= listLength // 2:
                    queue.append(currentNode)
                else:
                    stack.append(currentNode)
            currentNode = currentNode.next
            count += 1

        currentNode = head
        count = 1
        from_stack = True
        while count < listLength:
            if from_stack == True:
                currentNode.next = stack.pop()
            else:
                currentNode.next = queue.pop(0)
            count += 1
            from_stack = not from_stack
            currentNode = currentNode.next

        currentNode.next = None


# if [1,2,3]
# half queue, half stack
nodes = [2, 4, 6, 8]  # [2, 8, 4, 6]
# nodes = [0, 1, 2, 3, 4, 5, 6]  # [0, 6, 1, 5, 2, 4, 3]
currentNode = head = ListNode(nodes[0])
for i in range(1, len(nodes)):
    currentNode.next = ListNode(nodes[i])
    currentNode = currentNode.next


Solution.reorderList(None, head)
currentNode = head
while currentNode != None:
    print(currentNode.val)
    currentNode = currentNode.next
