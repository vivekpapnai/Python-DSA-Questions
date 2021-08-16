import queue


class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def constructBST(lst):
    if len(lst) == 0:
        return None
    l = len(lst)
    root_index = l -1 // 2
    root = BinaryTreeNode(lst[root_index])
    root.left = constructBST(lst[:root_index])
    root.right = constructBST(lst[root_index + 1:])
    return root

def preOrder(root):
    # Given a binary tree, print the preorder traversal of given tree. Pre-order
    # traversal is: Root LeftChild RightChild
    if root == None:
        return
    print(root.data, end=' ')
    preOrder(root.left)
    preOrder(root.right)


# Main
n = int(input())
if (n > 0):
    lst = [int(i) for i in input().strip().split()]
else:
    lst = []
root = constructBST(lst)
preOrder(root)
