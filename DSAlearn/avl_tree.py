class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.height = 1

class BalancedTree:
    def __init__(self):
        self.root = None

    def height(self, node: 'Node'):
        if not node:
            return 0
        return node.height

    def balance(self, node: 'Node'):
        if not node:
            return 0
        return self.height(node.left) - self.height(node.right)

    def rotateRight(self, y):
        x = y.left
        t2 = x.right

        x.right = y
        y.left = t2

        y.height = 1 + max((self.height(y.left), self.height(y.right)))
        x.height = 1 + max((self.height(x.left), self.height(x.right)))

        return x

    def rotateLeft(self, x):
        y = x.right
        t2 = y.left

        y.left = x
        x.right = t2

        x.height = 1 + max((self.height(x.left), self.height(x.right)))
        y.height = 1 + max((self.height(y.left), self.height(y.right)))

        return y

    def insertHelper(self, root, data):
        if not root:
            return Node(data)
        elif data > root.data:
            root.right = self.insertHelper(root.right, data)
        else:
            root.left = self.insertHelper(root.left, data)

        root.height = 1 + max(self.height(root.left), self.height(root.right))
        balance = self.balance(root)

        # Left-Left Case
        if balance > 1 and data < root.left.data:
            return self.rotateRight(root)

        # Right-Right Case
        if balance < -1 and data > root.right.data:
            return self.rotateLeft(root)

        # Left-Right Case
        if balance > 1 and data > root.left.data:
            root.left = self.rotateLeft(root.left)
            return self.rotateRight(root)

        # Right-Left Case
        if balance < -1 and data < root.right.data:
            root.right = self.rotateRight(root.right)
            return self.rotateLeft(root)

        return root

    def insert(self, data):
        self.root = self.insertHelper(self.root, data)

    def inorderTraversal(self, root: 'Node'):
        if root:
            self.inorderTraversal(root.left)
            print(root.data, end=' -> ')
            self.inorderTraversal(root.right)

    def printTree(self):
        self.inorderTraversal(self.root)


b1 = BalancedTree()
b1.insert(1)
b1.insert(3)
b1.insert(2)
b1.printTree()
