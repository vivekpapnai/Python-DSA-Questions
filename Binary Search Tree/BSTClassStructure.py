class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None
        self.numNodes = 0

    def IspresentHelper(self, root, data):
        if root is None:
            return False
        if root.data == data:
            return True
        if root.data > data:
            return self.IspresentHelper(root.left, data)
        else:
            return self.IspresentHelper(root.right, data)

    def InsertHelper(self, root, data):
        if root is None:
            root = BinaryTreeNode(data)
            return root
        if root.data >= data:
            root.left = self.InsertHelper(root.left, data)
        else:
            root.right = self.InsertHelper(root.right, data)
        return root
    def InsertData(self, data):
        self.root = self.InsertHelper(self.root,data)
        self.numNodes += 1
    def min(self,root):
        if root is None:
            return 10000000
        if root.left is None:
            return root.data
        return self.min(root.left)

    def deletedatahelper(self, root, data):
        if root is None:
            return False, None
        if root.data > data:
            Isdeleted, root.left = self.deletedatahelper(root.left, data)
            return Isdeleted, root
        if root.data < data:
            Isdeleted, root.right = self.deletedatahelper(root.right, data)
            return Isdeleted, root
        if root.data == data:
            if root.left is None and root.right is None:
                root = None
                return True, root
            elif root.left is None and root.right is not None:
                root.data = root.right.data
                return True, root

            elif root.right is None and root.left is not None:
                root.data = root.left.data
                return True, root
            else:
                replacemen = self.min(root.right)
                root.data = replacemen
                isdeleted,root.right = self.deletedatahelper(root.right,replacemen)
                return True, root

    def DeleteData(self, data):
        isdeleted, self.root = self.deletedatahelper(self.root,data)
        if isdeleted:
            self.numNodes -= 1
            return True
        else:
            return False
    def countnode(self):
        return self.numNodes

    def Ispresent(self, data):
        return self.IspresentHelper(self.root, data)

    def printtreehelper(self, root):
        if root is None:
            return None
        print(root.data, end=":")
        if root.left is not None:
            print("L", root.left.data, end=",")
        if root.right is not None:
            print("R", root.right.data, end=" ")
        print()
        self.printtreehelper(root.left)
        self.printtreehelper(root.right)

    def printTree(self):
        self.printtreehelper(self.root)



root = BST()
root.InsertData(10)
root.InsertData(5)
root.InsertData(15)
root.InsertData(13)
root.InsertData(7)
root.InsertData(3)
root.DeleteData(10)
root.printTree()

