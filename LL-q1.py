# Find the length of a linked list given test cases and linked list element return the length
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def printLL(head):
    while head is not None:
        print(head.data, end=" ")
        head = head.next


def LengthLL(head):
    count = 0
    while head is not None:
        count += 1
        head = head.next
    return count


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


t = int(input())
while t > 0:
    head = InputLL()
    print(LengthLL(head))
    # printLL(head)
    t -= 1
