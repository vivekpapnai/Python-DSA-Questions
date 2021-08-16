import queue
from sys import setrecursionlimit

setrecursionlimit(10 ** 6)


class treeNode:
    def __init__(self, data):
        self.data = data
        self.children = list()


def NodeWithMaxSum(root):
    if root is None:
        return None, 0
    max = root.data
    max_root = root
    for child in root.children:
        max += child.data
    for child in root.children:
        root_Node, sum = NodeWithMaxSum(child)
        if sum > max:
            max = sum
            max_root = root_Node
    return max_root, max


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
# PrintTree(root)
node, nodesum = NodeWithMaxSum(root)
print(node.data)
# print(CountLeafNode(root))
