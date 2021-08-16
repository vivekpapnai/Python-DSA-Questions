class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def printLL(head):
    while head.next is not None:
        print(head.data, end="->")
        head = head.next
    print(head.data)

def TakeInput():
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


head = TakeInput()
printLL(head)
