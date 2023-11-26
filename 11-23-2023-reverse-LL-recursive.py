# Given the head of a singly linked list, reverse the list, and return the reversed list.


# Example 1:

# Input: head = [1,2,3,4,5]
# Output: [5,4,3,2,1]


class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


def reverseList(head):
    if head == None or head.next == None:
        return head

    def listMaker(currNode, prevNode=None):
        if currNode == None:
            return prevNode
        else:
            reversed_node = Node(currNode.val)
            reversed_node.next = prevNode
            return listMaker(currNode.next, reversed_node)

    return listMaker(head)


head = Node(1)
two = Node(2)
three = Node(3)
four = Node(4)
five = Node(5)

head.next = two
two.next = three
three.next = four
four.next = five

print(reverseList(head).next.val)
