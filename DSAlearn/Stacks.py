class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            self.items.pop()
        else:
            raise Exception("Stack Is Empty")

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            raise Exception("Stack is Empty")

    def size(self):
        return len(self.items)

    def see_stack(self):
        return self.items


stack1 = Stack()
stack1.push(1)
stack1.push(2)
stack1.push(3)

print(stack1.see_stack())
stack1.pop()
print(stack1.see_stack())
print(stack1.size())
