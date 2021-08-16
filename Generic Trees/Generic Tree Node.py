class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = list()


def PrintTree(root):
    if root is None:
        return
    print(root.data, end=":")
    for i in root.children:
        print(i.data,",",end="")
    print()
    for child in root.children:
        PrintTree(child)


def Numnodes(root):
    if root is None:
        return 0
    count = 1
    for child in root.children:
        count = count + Numnodes(child)

    return count

def TakeInput():
    print("Enter the root element")
    rootdata = int(input())
    if rootdata ==-1:
        return None
    root = TreeNode(rootdata)
    print("Enter the total child of root",rootdata)
    k = int(input())
    for i in range(k):
        j = TakeInput()
        root.children.append(j)
    return root

root = TakeInput()
PrintTree(root)
print("Number of nodes are", Numnodes(root))