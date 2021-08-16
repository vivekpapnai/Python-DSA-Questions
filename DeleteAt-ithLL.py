from sys import setrecursionlimit
setrecursionlimit(10**6)

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def printLL(head):
    while head is not None:
        print(head.data, end=" ")
        head = head.next
    print()


def InsertLL():
    li = [int(x) for x in input().split()]
    head = None
    tail = head
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


def LengthLL(head):
    if head is None:
        return 0
    return 1 + LengthLL(head.next)


def DeleteNodeLL(head, position):
    if position < 0 or position >= LengthLL(head):
        return head
    prev = None
    count = 0
    curr = head
    nxt = head.next
    if position == 0:
        head = head.next
        return head
    while count < position:
        prev = curr
        curr = curr.next
        nxt = curr.next
        count += 1
    prev.next = nxt
    return head


def DeleteNodeRec(head, position):
    if position < 0:
        return head
    if head is None:
        return head
    if position ==0:
        head = head.next
        return head
    smallhead = DeleteNodeLL(head.next,position-1)
    head.next = smallhead
    return head

t = int(input())
while t > 0:
    head = InsertLL()
    position = int(input())
    # PrintLL(head)
    head = DeleteNodeRec(head, position)
    # head = DeleteNodeLL(head,position)
    printLL(head)
    t -= 1
