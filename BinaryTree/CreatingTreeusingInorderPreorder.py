import queue


class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def ConstructTreeUsingPreorderAndInorder(n, pre_order, in_order):
    if len(pre_order) == 0:
        return
    root = pre_order[0]
    root_index = in_order.index(root)
    left_inorder_sub_tree = in_order[0:root_index]
    right_inorder_sub_tree = in_order[root_index + 1:]
    left_l = len(left_inorder_sub_tree)
    left_preorder_sub_tree = pre_order[1:left_l + 1]
    right_preorder_sub_tree = pre_order[left_l + 1:]
    left_subTree = ConstructTreeUsingPreorderAndInorder(left_l, left_preorder_sub_tree, left_inorder_sub_tree)
    right_subTree = ConstructTreeUsingPreorderAndInorder(len(right_preorder_sub_tree), right_preorder_sub_tree,
                                                         right_inorder_sub_tree)
    root = BinaryTreeNode(root)
    root.left = left_subTree
    root.right = right_subTree
    return root


def TakeInput():
    li = [int(x) for x in input().split()]
    q = queue.Queue()
    start = 0
    if li[0] == -1:
        return None
    root = BinaryTreeNode(li[0])
    start += 1
    q.put(root)
    n = len(li)
    while not q.empty():
        curr = q.get()
        left_data = li[start]
        start += 1
        if left_data != -1:
            left_node = BinaryTreeNode(left_data)
            curr.left = left_node
            q.put(left_node)
        right_data = li[start]
        start += 1
        if right_data != -1:
            right_node = BinaryTreeNode(right_data)
            curr.right = right_node
            q.put(right_node)
    return root


def printLevelWise(root):
    if root is None:
        return

    pendingNodes = queue.Queue()
    pendingNodes.put(root)
    pendingNodes.put(None)

    while not pendingNodes.empty():
        frontNode = pendingNodes.get()

        if frontNode is None:
            print()

            if not pendingNodes.empty():
                pendingNodes.put(None)

        else:
            print(frontNode.data, end=" ")

            if frontNode.left is not None:
                pendingNodes.put(frontNode.left)

            if frontNode.right is not None:
                pendingNodes.put(frontNode.right)


n = int(input())
pre_order = [int(x) for x in input().split()]
in_order = [int(x) for x in input().split()]
root = ConstructTreeUsingPreorderAndInorder(n, pre_order, in_order)
printLevelWise(root)
