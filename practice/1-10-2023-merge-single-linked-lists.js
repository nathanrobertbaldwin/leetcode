// You are given the heads of two sorted linked lists list1 and list2.

// Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.

// Return the head of the merged linked list.

class ListNode {
    constructor(val, next = null) {
        this.val = val;
        this.next = next;
    }
}

class LinkedList {

    constructor() {
        this.head = null;
        this.length = 0;
    }

    addToHead(val) {
        const newNode = new ListNode(val);

        if (!(this.head)) {
            this.head = newNode;
        } else {
            newNode.next = this.head;
            this.head = newNode;
        }
        this.length++;
    }
}

let mergeTwoLists = function (list1, list2) {

    if (!list1 && !list2) return null;
    if (!list1) return list2;
    if (!list2) return list1;

    let newListHead;

    if (list1.val <= list2.val) {
        const newNode = new ListNode(list1.val);
        newListHead = newNode;
        list1 = list1.next;
    } else {
        const newNode = new ListNode(list2.val);
        newListHead = newNode;
        list2 = list2.next;
    }

    let currNodeNewList = newListHead;

    while (list1 || list2) {

        if (!list1) {
            const newNode = new ListNode(list2.val);
            currNodeNewList.next = newNode;
            currNodeNewList = currNodeNewList.next;
            list2 = list2.next;
            continue;
        } else if (!list2) {
            const newNode = new ListNode(list1.val);
            currNodeNewList.next = newNode;
            currNodeNewList = currNodeNewList.next;
            list1 = list1.next;
            continue;
        }

        if (list1.val <= list2.val) {
            const newNode = new ListNode(list1.val);
            currNodeNewList.next = newNode;
            currNodeNewList = currNodeNewList.next;
            list1 = list1.next;
        } else {
            const newNode = new ListNode(list2.val);
            currNodeNewList.next = newNode;
            currNodeNewList = currNodeNewList.next;
            list2 = list2.next;
        }
    }

    return newListHead;

};

function makeList(array) {

    array.reverse();

    const list = new LinkedList();

    array.forEach(element => {
        list.addToHead(element);
    });

    return list;
}

listArr1 = [1, 1, 4]
listArr2 = [2, 3, 4]

list1 = makeList(listArr1);
list2 = makeList(listArr2);

console.log(mergeTwoLists(list1.head, list2.head))

// [1,1,2,3,4,4]
