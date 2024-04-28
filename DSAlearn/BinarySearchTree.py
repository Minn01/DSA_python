class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self) -> None:
        self.root = None

    def insertHelper(self, root: 'Node', node: 'Node') -> 'Node':
        if not root:
            return node
        elif root.data < node.data:
            root.right = self.insertHelper(root.right, node)
        else:
            root.left = self.insertHelper(root.left, node)
        return root

    def insert(self, data) -> None:
        new_node = Node(data)
        self.root = self.insertHelper(self.root, new_node)

    def displayHelper(self, root: 'Node') -> None:
        if root:
            self.displayHelper(root.left)
            print(root.data, end=" ")
            self.displayHelper(root.right)

    def display(self) -> None:
        self.displayHelper(self.root)
        print()

    def searchHelper(self, root: 'Node', data):
        if not root:
            return False
        elif root.data == data:
            return True
        elif root.data < data:
            return self.searchHelper(root.right, data)
        else:
            return self.searchHelper(root.left, data)

    def search(self, data) -> bool:
        return self.searchHelper(self.root, data)

    @staticmethod
    def successor(root: 'Node'):
        while root.left:
            root = root.left
        return root.data

    @staticmethod
    def predecessor(root: 'Node'):
        while root.right:
            root = root.right
        return root.data

    def removeHelper(self, root: 'Node', data) -> 'Node':
        if not root:
            return root
        elif root.data < data:
            root.right = self.removeHelper(root.right, data)
        elif root.data > data:
            root.left = self.removeHelper(root.left, data)
        else:
            # Handling cases with one or no child nodes
            if not root.right:
                return root.left
            elif not root.left:
                return root.right

            # Handling the case with two child nodes
            root.data = self.successor(root.right)
            root.right = self.removeHelper(root.right, root.data)
        return root

    def remove(self, data) -> None:
        if not self.search(data):
            print(data, "not found!")
        else:
            self.root = self.removeHelper(self.root, data)

    def __str__(self) -> str:
        return f"({self.display()})"


bTree = BinarySearchTree()
bTree.insert(4)
bTree.insert(2)
bTree.insert(1)
bTree.insert(3)
bTree.insert(7)
bTree.insert(6)
bTree.insert(9)
bTree.display()

print(bTree.search(-1))
bTree.remove(7)
bTree.insert(11)
bTree.display()
