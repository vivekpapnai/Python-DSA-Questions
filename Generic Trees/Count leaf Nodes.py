import queue
from sys import setrecursionlimit
setrecursionlimit(10**6)

class treeNode:
    def __init__(self, data):
        self.data = data
        self.children = list()


def CountLeafNode(root):
    if root is None:
        return 0
    count = 0
    if len(root.children) == 0:
        count += 1
        return count
    for child in root.children:
        temp = CountLeafNode(child)
        count += temp
    return count


def LevelWiseInput(arr):
    i = 0
    q = queue.Queue()
    rootdata = arr[i]
    i += 1
    root = treeNode(rootdata)
    q.put(root)
    while not q.empty():
        curr_node = q.get()
        children_node = arr[i]
        i += 1
        for j in range(children_node):
            childNode = treeNode(arr[i + j])
            curr_node.children.append(childNode)
            q.put(childNode)
        i += children_node
    return root


def PrintTree(root):
    q = queue.Queue()
    q.put(root)
    while q:
        parent = q.get()
        print(parent.data, ":", ",".join(str(x.data) for x in parent.children), sep="")
        for child in parent.children:
            q.put(child)


arr = [int(x) for x in input().split()]
root = LevelWiseInput(arr)
PrintTree(root)
# print(CountLeafNode(root))
