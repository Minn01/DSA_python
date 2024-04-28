class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __str__(self) -> str:
        return f"Node[data={self.data}, next={self.next}]"

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return

        current_node: 'Node' = self.head
        while current_node.next is not None:
            current_node = current_node.next

        current_node.next = new_node

    def count(self, data) -> int:
        count = 0
        current_node: 'Node' = self.head
        while current_node is not None:
            if data == current_node.data:
                count += 1
            current_node = current_node.next
        return count

    def print_list(self) -> None:
        current_node: 'Node' = self.head
        while current_node is not None:
            print(current_node.data, end=" -> ")
            current_node = current_node.next
        print(None)

    def remove(self, data) -> None:
        current_node: 'Node' = self.head
        while current_node.next.data != data:
            current_node = current_node.next
        current_node.next = current_node.next.next

    def accessNode(self, index):
        index_count = 0
        current_node = self.head
        while index_count != index:
            index_count += 1
            current_node = current_node.next
        return current_node.data

    def __len__(self) -> int:
        count = 0
        current_node = self.head
        while current_node is not None:
            count += 1
            current_node = current_node.next
        return count

    def __iter__(self):
        current_node: 'Node' = self.head
        while current_node is not None:
            yield current_node.data
            current_node = current_node.next


# Create a linked list
lis = LinkedList()

# Append elements
lis.append(1)
lis.append(2)
lis.append(3)
lis.append(3)
lis.append(3)
lis.append(2)

print("Nodes: ", len(lis))

print("Loop : \n")
for i in lis:
    print(i)
print()

# Print the linked list
lis.print_list()  # Output: 1 -> 2 -> 3 -> None

print(lis.count(2))
print(lis.count(3))

lis.remove(3)
lis.print_list()
print(lis.accessNode(3))
