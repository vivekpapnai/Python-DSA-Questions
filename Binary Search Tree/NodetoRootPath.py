import queue
from sys import stdin

class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def NodetoRootPath(root,x):
    if root is None:
        return None
    if root.data == x:
        li = list()
        li.append(root.data)
        return li
    leftpath = NodetoRootPath(root.left,x)
    if leftpath !=None:
        leftpath.append(root.data)
        return leftpath
    RightPath = NodetoRootPath(root.right,x)
    if RightPath != None:
        RightPath.append(root.data)
        return RightPath
    else:
        return None

def PrintBinaryTree(root):
    if root is None:
        return None
    print(root.data, end=":")
    if root.left is not None:
        print("L", root.left.data, end=",")
    if root.right is not None:
        print("R", root.right.data, end=" ")
    print()
    PrintBinaryTree(root.left)
    PrintBinaryTree(root.right)


def takeInput():
    levelOrder = list(map(int, stdin.readline().strip().split(" ")))
    start = 0

    length = len(levelOrder)

    root = BinaryTreeNode(levelOrder[start])
    start += 1

    q = queue.Queue()
    q.put(root)

    while not q.empty():
        currentNode = q.get()

        leftChild = levelOrder[start]
        start += 1

        if leftChild != -1:
            leftNode = BinaryTreeNode(leftChild)
            currentNode.left = leftNode
            q.put(leftNode)

        rightChild = levelOrder[start]
        start += 1

        if rightChild != -1:
            rightNode = BinaryTreeNode(rightChild)
            currentNode.right = rightNode
            q.put(rightNode)

    return root

root = takeInput()
x = int(input())
# PrintBinaryTree(root)
li = NodetoRootPath(root,x)
print(li)
# for i in li:
#     print(i ,end=" ")