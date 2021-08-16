# insert at element at ith position in a linked list
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def InputLL():
    li = [int(x) for x in input().split()]
    head = None
    tail = None
    for currdata in li:
        if currdata == -1:
            break
        else:
            NewNode = Node(currdata)
            if head is None:
                head = NewNode
                tail = head
            else:
                tail.next = NewNode
                tail = tail.next
    return head


def printLL(head):
    while head is not None:
        print(head.data, end=" ")
        head = head.next
    print()


def InsertRecursively(head, i, data):
    if i<0:
        return head
    if i == 0:
        data = Node(data)
        data.next = head
        head = data
        return head
    if head is None:
        return head
    smallhead = InsertRecursively(head.next, i - 1, data)
    head.next = smallhead
    return head


def InsertAtith(head, i, data):
    count = 0
    tail = head
    data = Node(data)
    if i == 0:
        temp = head
        head = data
        data.next = temp
        return head

    while tail is not None:
        if count == i - 1:
            temp = tail.next
            tail.next = data
            data.next = temp
            break
        count += 1
        tail = tail.next
        # prev = prev.next
    return head


def lengthLL(head):
    count = 0
    while head is not None:
        count += 1
        head = head.next
    return count


def DeleteNodeatith(head, i):
    if i < 0 or i >= lengthLL(head):
        return head
    count = 0
    prev = None
    curr = head
    curr_next = head.next
    if i == 0:
        head = head.next
        return head
    while count < i:
        prev = curr
        curr = curr.next
        curr_next = curr.next
        count += 1
    prev.next = None
    curr.next = None
    prev.next = curr_next
    return head


t = int(input())
while t > 0:
    head = InputLL()
    i = int(input())  # the position where the element is needed to be inserted
    data = int(input())
    printLL(head)
    head = InsertRecursively(head, i, data)
    printLL(head)
    t -= 1
