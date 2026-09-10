class Stack:
    def __init__(self):
        self.elements = []

    def is_empty(self):
        return len(self.elements) == 0

    def is_full(self):
        return False  # In Python, a list can grow dynamically, so we don't have a fixed size

    def push(self, item):
        self.elements.insert(0, item)  # Insert at the front of the list to simulate stack behavior

    def pop(self):
        if self.is_empty():
            print("*** The stack is empty")
            return
        else:
            return self.elements.pop(0)

    def peek(self):
        if self.is_empty():
            print("*** The stack is empty")
            return
        else:
            return self.elements[0]

s = Stack()
print(f"Is the stack empty? {s.is_empty()}")

print(f"Pop from the stack: {s.pop()}")  # This will print a message since the stack is empty
print(f"Peek at the top element: {s.peek()}")  # This will print a message since the stack is empty

s.push(10)
print(f"Peek at the top element after pushing 10: {s.peek()}")
print(f"Is the stack empty? {s.is_empty()}")

s.push(20)
print(f"Peek at the top element after pushing 20: {s.peek()}")
s.push(30)
print(f"Peek at the top element after pushing 30: {s.peek()}")
s.push(40)
s.push(50)
print(f"Peek at the top element after pushing 50: {s.peek()}")

print(f"Pop from the stack: {s.pop()}")
print(f"Pop from the stack: {s.pop()}")
print(f"Pop from the stack: {s.pop()}")
print(f"Pop from the stack: {s.pop()}")
print(f"Is the stack empty? {s.is_empty()}")
print(f"Peek at the top element: {s.peek()}")
print(f"Pop from the stack: {s.pop()}")
print(f"Is the stack empty? {s.is_empty()}")
print(f"Peek at the top element: {s.peek()}")