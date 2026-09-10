class Stack:
    def __init__(self):
        self.max_size = 5  # Set the maximum size for this stack implementation
        self.elements = [None] * self.max_size  # Initialize the elements list with a fixed size
        self.i = -1  # Initialize the index to -1

    def is_empty(self):
        return self.i == -1

    def is_full(self):
        return self.i >= self.max_size - 1

    def push(self, item):
        if self.is_full():
            print("*** Stack is full. Cannot push item.")
        else:
            self.i += 1
            self.elements[self.i] = item

    def pop(self):
        if self.is_empty():
            print("*** The stack is empty")
            return -1
        else:
            item = self.elements[self.i]
            self.i -= 1
            return item

    def peek(self):
        if self.is_empty():
            print("*** The stack is empty")
            return -1
        else:   
            return self.elements[self.i]

s = Stack()
print(f"Is the stack empty? {s.is_empty()}")
print(f"Is the stack full? {s.is_full()}")


print(f"Pop from the stack: {s.pop()}")  # This will print a message since the stack is empty
print(f"Peek at the top element: {s.peek()}")  # This will print a message since the stack is empty

s.push(10)
print(f"Peek at the top element after pushing 10: {s.peek()}")
print(f"Is the stack empty? {s.is_empty()}")
print(f"Is the stack full? {s.is_full()}")
s.push(20)
print(f"Peek at the top element after pushing 20: {s.peek()}")
s.push(30)
print(f"Peek at the top element after pushing 30: {s.peek()}")
s.push(40)
s.push(50)
print(f"Peek at the top element after pushing 50: {s.peek()}")
print(f"Is the stack empty? {s.is_empty()}")
print(f"Is the stack full? {s.is_full()}")
s.push(60)  # This will print a message since the stack is full


print(f"Pop from the stack: {s.pop()}")
print(f"Pop from the stack: {s.pop()}")
print(f"Pop from the stack: {s.pop()}")
print(f"Pop from the stack: {s.pop()}")
print(f"Is the stack empty? {s.is_empty()}")
print(f"Peek at the top element: {s.peek()}")
print(f"Pop from the stack: {s.pop()}")
print(f"Is the stack empty? {s.is_empty()}")
print(f"Peek at the top element: {s.peek()}")

