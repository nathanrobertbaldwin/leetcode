def swapPairs(head):
    if head == None or head.next == None:
        return head

    newHead = head.next

    def swapper(currNode, past_left=None):
        if currNode != None and currNode.next != None:
            left = currNode
            right = currNode.next
            later = currNode.next.next
            left.next = later
            right.next = left
            if past_left != None:
                past_left.next = right
                past_left = left

            swapper(later, left)

    swapper(head)
    return newHead


class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


head = Node(1)
two = Node(2)
three = Node(3)
four = Node(4)
five = Node(5)

head.next = two
two.next = three
three.next = four
four.next = five

print(swapPairs(head).next.next.next.next.next)
