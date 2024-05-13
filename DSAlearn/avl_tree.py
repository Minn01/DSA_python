class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.height = 1

class BalancedTree:
    def __init__(self):
        self.root = None

    @staticmethod
    def height(root: 'Node'):
        if not root:
            return 0
        else:
            return root.height

    def balance(self, root: 'Node'):
        if not root:
            return 0
        else:
            return self.height(root.left) - self.height(root.right)

    def rotate_right(self, y: 'Node'):
        x = y.left
        t2 = x.right

        y.left = t2
        x.right = y

        y.height = max(self.height(y.left), self.height(y.right))
        x.height = max(self.height(x.left), self.height(x.right))

        return x

    def rotate_left(self, x):
        y = x.right
        t2 = y.left

        x.right = t2
        y.left = x

        x.height = max(self.height(x.left), self.height(x.right))
        y.height = max(self.height(y.left), self.height(y.right))

        return y

    def insertHelper(self, root: 'Node', data):
        if not root:
            return Node(data)
        elif data < root.data:
            root.left = self.insertHelper(root.left, data)
        else:
            root.right = self.insertHelper(root.right, data)

        root.height = 1 + max(self.height(root.left), self.height(root.right))
        balance = self.balance(root)

        # Left Cases
        if balance > 1:
            # Left-Left Case
            if data < root.left.data:
                return self.rotate_right(root)
            # Right-Right Case
            elif data > root.left.data:
                root.left = self.rotate_left(root.left)
                return self.rotate_right(root)
        # Right Cases
        elif balance < -1:
            # Right-Right Case
            if data > root.right.data:
                return self.rotate_left(root)
            # Right-Left Case
            elif data > root.right.data:
                root.right = self.rotate_right(root.right)
                return self.rotate_left(root)

        return root

    def insert(self, data) -> None:
        self.root = self.insertHelper(self.root, data)

    def insert_many(self, *datas):
        for i in datas:
            self.insert(i)

    def inorder_traversal(self, root: 'Node') -> None:
        if root:
            self.inorder_traversal(root.left)
            print(root.data, end=" -> ")
            self.inorder_traversal(root.right)

    def printTree(self) -> None:
        self.inorder_traversal(self.root)
        print(None)

    def search_helper(self, root, data) -> bool:
        if not root:
            return False
        elif data < root.data:
            return self.search_helper(root.left, data)
        elif data > root.data:
            return self.search_helper(root.right, data)
        else:
            return True

    def search(self, data):
        return self.search_helper(self.root, data)

    @staticmethod
    def inorder_successor(root: 'Node'):
        while root.left:
            root = root.left
        return root.data

    def remove_helper(self, root: 'Node', data):
        if not root:
            return root
        elif data < root.data:
            root.left = self.remove_helper(root.left, data)
        elif data > root.data:
            root.right = self.remove_helper(root.right, data)
        else:
            # Handling cases for one or no child nodes
            if not root.left:
                return root.right
            elif not root.right:
                return root.left

            # Handling cases for two child nodes
            root.data = self.inorder_successor(root.right)
            root.right = self.remove_helper(root.right, root.data)

            root.height = 1 + max(self.height(root.left), self.height(root.right))
            balance = self.balance(root)

            # Re-balancing the tree
            if balance > 1:  # Left Cases
                # Left-Left Case
                if data < root.left.data:
                    return self.rotate_right(root)
                # Left-Right Case
                elif data > root.left.data:
                    root.left = self.rotate_left(root.left)
                    return self.rotate_right(root)
            # Right Cases
            elif balance < -1:
                # Right-Right Case
                if data > root.right.data:
                    return self.rotate_left(root)
                # Right-Left Case
                elif data > root.right.data:
                    root.right = self.rotate_right(root.right)
                    return self.rotate_left(root)

        return root

    def remove(self, data):
        if self.search(data):
            self.root = self.remove_helper(self.root, data)
        else:
            raise Exception("Data to be removed not found!")

    def remove_many(self, *datas):
        for i in datas:
            self.remove(i)


b1 = BalancedTree()
# b1.insert(3)
# b1.insert(2)
# b1.insert(1)
# b1.insert(5)
# b1.insert(6)
# b1.insert(4)
b1.insert_many(10, 5, 15, 3, 7, 12, 20, 1, 4, 6, 9, 11, 14, 18, 25)
b1.printTree()
b1.remove_many(7, 15, 5, 10, 18, 1, 20)
b1.printTree()


# # Left-Left Case
        # if balance > 1 and data < root.left.data:
        #     return self.rotate_right(root)
        # # Right-Right Case
        # if balance < -1 and data > root.right.data:
        #     return self.rotate_left(root)
        # # Left-Right Case
        # if balance > 1 and data > root.left.data:
        #     root.left = self.rotate_left(root.left)
        #     return self.rotate_right(root)
        # # Right-Left Case
        # if balance < -1 and data < root.right.data:
        #     root.right = self.rotate_right(root.right)
        #     return self.rotate_left(root)
