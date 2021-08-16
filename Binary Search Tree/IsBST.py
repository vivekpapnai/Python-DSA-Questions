import queue
from sys import stdin

class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def minofTree(root):
    if root is None:
        return 100000
    leftmin = minofTree(root.left)
    rightmin = minofTree(root.right)
    min1 = min(leftmin, rightmin, root.data)
    return min1


def maxodTree(root):
    if root is None:
        return -100000
    leftmax = maxodTree(root.left)
    rightmax = maxodTree(root.right)
    max1 = max(leftmax, rightmax, root.data)
    return max1


def isBST(root):
    if root is None:
        return True
    left_max = maxodTree(root.left)
    right_min = minofTree(root.right)
    if left_max >= root.data or right_min < root.data:
        return False
    is_left_BST = isBST(root.left)
    is_right_BST = isBST(root.right)
    return is_left_BST and is_right_BST

def isBSTBetter(root):
    if root is None:
        return 100000, -100000, True
    Left_Min, Left_Max, IsleftBST = isBSTBetter(root.left)
    Right_Min, Right_Max ,IsrightBST = isBSTBetter(root.right)
    minimum = min(Left_Min,Right_Min,root.data)
    maximum = max(Left_Max,Right_Max,root.data)
    isBstTrue = True
    if root.data <= Left_Max or root.data > Right_Min:
        isBstTrue = False
    if not(IsleftBST) or not(IsrightBST):
        isBstTrue = False
    return minimum,maximum,isBstTrue

def isBST3(root,min_range =-100000,max_range = 100000):
    if root is None:
        return True
    if root.data < min_range or root.data >max_range:
        return False
    IsLeftBSt = isBST3(root.left,min_range,root.data-1)
    IsRightBSt = isBST3(root.right,root.data,max_range)
    return IsLeftBSt and IsRightBSt


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
# if isBST(root):
#     print("true")
# else:
#     print("false")
# PrintBinaryTree(root)
# print(isBSTBetter(root))
PrintBinaryTree(root)
print(isBST3(root))