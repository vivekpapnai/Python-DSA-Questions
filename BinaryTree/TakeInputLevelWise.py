from sys import setrecursionlimit
import queue

setrecursionlimit(10 ** 6)


class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


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


def TakeinputLevelWise():
    root_data = int(input("enter root"))
    q = queue.Queue()
    if root_data == -1:
        return None
    root = BinaryTreeNode(root_data)
    q.put(root)
    while not q.empty():
        curr_node = q.get()
        print("enter left child of", curr_node.data)
        leftchild = int(input())
        if leftchild != -1:
            leftnode = BinaryTreeNode(leftchild)
            curr_node.left = leftnode
            q.put(leftnode)
        print("enter right child of", curr_node.data)
        rightchild = int(input())
        if rightchild != -1:
            rightnode = BinaryTreeNode(rightchild)
            curr_node.right = rightnode
            q.put(rightnode)
    return root


def PrintLEvelWise(root):
    if root is None:
        return
    q = queue.Queue()
    q.put(root)
    while not q.empty():
        curr_ele = q.get()
        print(curr_ele.data, end=" ")
        if curr_ele.left is not None:
            q.put(curr_ele.left)
        if curr_ele.right is not None:
            q.put(curr_ele.right)

def TakeInputLevelWiseInARow():
    arr =[int(x) for x in input().split()]
    start = 0
    if len(arr) ==1:
        return None
    q = queue.Queue()
    root = BinaryTreeNode(arr[start])
    q.put(root)
    start += 1
    while not q.empty():
        curr_node = q.get()
        leftdata = arr[start]
        start += 1
        if leftdata != -1:
            leftnode = BinaryTreeNode(leftdata)
            curr_node.left = leftnode
            q.put(leftnode)
        rightdata = arr[start]
        start += 1
        if rightdata != -1:
            rightnode = BinaryTreeNode(rightdata)
            curr_node.right = rightnode
            q.put(rightnode)
    return root


root = TakeInputLevelWiseInARow()
PrintLEvelWise(root)
# PrintBinaryTree(root)