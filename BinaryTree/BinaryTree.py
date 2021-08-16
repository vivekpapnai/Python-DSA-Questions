class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def PrintBinaryTree(root):
    if root is None:
        return
    print(root.data, end=":")
    if root.left is not None:
        print("L", root.left.data, end=",")
    if root.right is not None:
        print("R", root.right.data, end=" ")
    print()
    PrintBinaryTree(root.left)
    PrintBinaryTree(root.right)


def InputTree():
    root = int(input())
    if root == -1: # if user enter -1 it means it is None so we will return
        return
    root = BinaryTreeNode(root) #the input format will be first enter root then it's left child then left's child
    lefttree = InputTree()
    righttree = InputTree()
    root.left = lefttree
    root.right = righttree
    return root


root = InputTree()
PrintBinaryTree(root)
