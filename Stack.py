class Stack(object):
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            raise IndexError("pop from empty stack")

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            raise IndexError("peek from empty stack")

    def size(self):
        return len(self.items)


s = Stack()
print(s.is_empty())  # Output: True
s.push(1)
s.push(2)
print(s.pop())  # Output: 2
print(s.peek())  # Output: 1
print(s.size())  # Output: 1

