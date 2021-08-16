# For a given a singly linked list of integers and a position 'i',
# print the node data at the 'i-th' position.
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def LengthLL(head):
    count = 0
    while head is not None:
        count += 1
        head = head.next
    return count


def Printith(head, i):
    length = LengthLL(head)
    if length < i:
        print("Not possible to print")
        return
    else:
        count = 0
        while head is not None:
            if count ==i:
                print(head.data)
                break
            count += 1
            head = head.next
        # return head.data

def InputLL():
    li = [int(x) for x in input().split()]
    head = None
    tail = None
    for currdata in li:
        if currdata==-1:
            break
        else:
            Newnode = Node(currdata)
            if head is None:
                head = Newnode
                tail  = head
            else:
                tail.next = Newnode
                tail = tail.next
    return head


t = int(input())
while t > 0:
    head = InputLL()
    i = int(input())
    Printith(head,i)
    t -= 1
