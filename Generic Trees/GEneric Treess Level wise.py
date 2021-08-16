import queue


class treeNode:
    def __init__(self, data):
        self.data = data
        self.children = list()


def TakeInputLevelWise(arr):
    if len(arr) == 0:
        return None
    q = queue.Queue()
    i = 0
    rootdata = arr[i]
    i += 1
    root = treeNode(rootdata)
    q.put(root)
    while not q.empty():
        curr_node = q.get()
        rn = arr[i]
        i += 1
        for j in range(rn):
            childrennode = treeNode(arr[i + j])
            curr_node.children.append(childrennode)
            q.put(childrennode)
        i += rn
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
root = TakeInputLevelWise(arr)
PrintTree(root)
