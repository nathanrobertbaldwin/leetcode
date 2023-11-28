class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def merged_lists(list1, list2):
    def merger(list1, list2, merged):
        if list1 != None and list2 != None:
            if list1.val <= list2.val:
                merged.next = ListNode(list1.val)
                return merger(list1.next, list2, merged.next)
            else:
                merged.next = ListNode(list2.val)
                return merger(list1, list2.next, merged.next)
        elif list1 != None and list2 == None:
            merged.next = ListNode(list1.val)
            return merger(list.next, list2, merged.next)
        elif list1 == None and list2 != None:
            merged.next = ListNode(list2.val)
            return merger(list1, list2.next, merged.next)
        else:
            return merged

    new_list = ListNode(1)
    merger(list1, list2, new_list)
    return new_list.next


lesser = None

greater = ListNode(1)

print(merged_lists(lesser, greater).val)
