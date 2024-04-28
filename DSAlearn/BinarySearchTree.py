class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.left = None
        self.right = None

# class BinarySearchTree:
#     def __init__(self):
#         self.root = None
#
#     def insertHelper(self, root: 'Node', node: 'Node') -> 'Node':
#         if not root:
#             return node
#         elif node.data < root.data:
#             root.left = self.insertHelper(root.left, node)
#         else:
#             root.right = self.insertHelper(root.right, node)
#
#         return root
#
#     def insert(self, data) -> None:
#         new_node = Node(data)
#         self.root = self.insertHelper(self.root, new_node)
#
#     def displayHelper(self, root: 'Node') -> None:
#         if root:
#             self.displayHelper(root.left)
#             print(root.data, end=" ")
#             self.displayHelper(root.right)
#
#     def display(self) -> None:
#         self.displayHelper(self.root)
#         print()
#
#     def searchHelper(self, root: 'Node', data) -> bool:
#         if not root:
#             return False
#         elif root.data == data:
#             return True
#         elif root.data < data:
#             return self.searchHelper(root.right, data)
#         else:
#             return self.searchHelper(root.left, data)
#
#     def search(self, data) -> bool:
#         return self.searchHelper(self.root, data)
#
#     def successor(self, root: 'Node'):
#         current_root = root.right
#         while current_root.left:
#             current_root = current_root.left
#         return current_root.data
#
#     def predecessor(self, root: 'Node'):
#         current_root = root.left
#         while current_root.right:
#             current_root = current_root.right
#         return current_root
#
#     def removeHelper(self, root: 'Node', data):
#         if not root:
#             return root
#         elif data < root.data:
#             root.left = self.removeHelper(root.left, data)
#         elif data > root.data:
#             root.right = self.removeHelper(root.right, data)
#         else:
#             # Node with only one child or no child
#             if not root.left:
#                 return root.right
#             elif not root.right:
#                 return root.left
#
#             # Node with two children: Get the inorder successor (smallest in the right subtree)
#             root.data = self.successor(root.right)
#
#             # Delete the inorder successor
#             root.right = self.removeHelper(root.right, root.data)
#
#         return root
#
#     def remove(self, data):
#         if self.search(data):
#             self.removeHelper(self.root, data)
#         else:
#             print(data, " could not be found!")

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insertHelper(self, root: 'Node', node: 'Node'):
        if not root:
            return node
        elif root.data < node.data:
            root.right = self.insertHelper(root.right, node)
        else:
            root.left = self.insertHelper(root.left, node)
        return root

    def insert(self, data):
        new_node = Node(data)
        self.root = self.insertHelper(self.root, new_node)

    def displayHelper(self, root: 'Node'):
        if root:
            self.displayHelper(root.left)
            print(root.data, end=" ")
            self.displayHelper(root.right)

    def display(self):
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

    def search(self, data):
        return self.searchHelper(self.root, data)

    # @staticmethod
    # def successor(root: 'Node'):
    #     while root.left:
    #         root = root.left
    #     return root.data

    # @staticmethod
    # def predecessor(root: 'Node'):
    #     while root.right:
    #         root = root.right
    #     return root.data

    # def removeHelper(self, root: 'Node', data):
    #     if not root:
    #         return root
    #     elif root.data < data:
    #         root.right = self.removeHelper(root.right, data)
    #     elif root.data > data:
    #         root.left = self.removeHelper(root.left, data)
    #     else:
    #         # Handling cases with one or no child nodes
    #         if not root.right:
    #             return root.left
    #         elif not root.left:
    #             return root.right
    #
    #         # Handling the case with two child nodes
    #         root.data = self.successor(root.right)
    #         root.right = self.removeHelper(root.right, root.data)
    #     return root
    #
    # def remove(self, data):
    #     if not self.search(data):
    #         print(data, "not found!")
    #     else:
    #         self.root = self.removeHelper(self.root, data)

    @staticmethod
    def successor(root: 'Node'):
        while root.left:
            root = root.left
        return root.data

    def removeHelper(self, root: 'Node', data):
        if not root:
            return root
        elif root.data < data:
            root.right = self.removeHelper(root.right, data)
        elif root.data > data:
            root.left = self.removeHelper(root.left, data)
        else:
            if not root.right:
                return root.left
            elif not root.left:
                return root.right

            root.data = self.successor(root.right)
            root.right = self.removeHelper(root.right, root.data)

        return root

    def remove(self, data):
        if self.search(data):
            self.root = self.removeHelper(self.root, data)
        else:
            print(data, "not found!")

    def __str__(self):
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
bTree.display()
