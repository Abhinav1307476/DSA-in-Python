class Back_Stack:
    def __init__(self):
        self.bottom=0
        self.top=-1 # Initialize the index to -1
        self.max_size=5 # Set the maximum size for this stack implementation
        self.stack=[None]*self.max_size # Initialize the elements list with a fixed size
    
    def is_empty(self):
        return self.top==-1
    
    def is_full(self):
        return self.top+1>=self.max_size
    
    def push(self,data):
        if self.is_full():
            print("Stack is full")
            return
        for i in range(self.top,-1,-1):
            self.stack[i+1]=self.stack[i]
        self.stack[self.bottom]=data
        self.top+=1
        
    def pop(self):
        if self.is_empty():
            print("Stack is empty")
            return -1
        item=self.stack[self.bottom]
        for i in range(self.bottom,self.top):
            self.stack[i]=self.stack[i+1]
        self.top-=1
        return item
    
    def peek(self):
        if self.is_empty():
            print("Stack is empty")
            return -1
        return self.stack[self.bottom]

s = Back_Stack()
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