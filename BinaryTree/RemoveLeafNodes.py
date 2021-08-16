from sys import stdin, setrecursionlimit
import queue
setrecursionlimit(10 ** 6)

class BinaryTreeNode:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

def takeInput():
    levelOrder = list(map(int, stdin.readline().strip().split(" ")))
    start = 0

    length = len(levelOrder)

    if length == 1:
        return None

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

def PrintBinaryTree(root):
    if root is None:
        return
    print(root.data,end=":")
    if root.left is not None:
        print("L",root.left.data, end=",")
    if root.right is not None:
        print("R",root.right.data, end="")
    print()
    PrintBinaryTree(root.left)
    PrintBinaryTree(root.right)

def RemoveLeafNode(root):
    if root is None:
        return
    if root.left is None and root.right is None:
        return None
    root.left = RemoveLeafNode(root.left)
    root.right = RemoveLeafNode(root.right)

    return root

root = takeInput()
PrintBinaryTree(root)
root = RemoveLeafNode(root)
PrintBinaryTree(root)
