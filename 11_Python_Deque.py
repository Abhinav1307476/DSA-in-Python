class Deque:
    def __init__(self):
        self.elements = []

    def is_empty(self):
        return len(self.elements) == 0

    def addRear(self, item):
        self.elements.append(item) # append, inserts at the end of the list

    # add feature to add an item to the front of the deque
    def addFront(self, item):
        self.elements.insert(0, item) # insert at the front of the list

    def removeFront(self):
        if self.is_empty():
            return
        else:
            return self.elements.pop(0)
    # add feature to remove an item from the rear of the deque
    def removeRear(self):
        if self.is_empty():
            return
        else:
            return self.elements.pop()
        
    def peek(self):
        if self.is_empty():
            return
        return self.elements[0]


q = Deque()
print(f"Is the deque empty? {q.is_empty()}")
print(f"Remove from the rear of the deque: {q.removeRear()}")  # This will print a message since the deque is empty
print(f"Remove from the front of the deque: {q.removeFront()}")  # This will print a message since the deque is empty
print(f"Peek at the front element of the deque: {q.peek()}")  # This will print a message since the deque is empty

q.addRear(10)
print(f"Peek at the front element after adding to the rear: {q.peek()}")
q.addRear(20)
print(f"Peek at the front element after adding to the rear: {q.peek()}")
q.addFront(8)
print(f"Peek at the front element after adding to the front: {q.peek()}")
q.addFront(5)
print(f"Peek at the front element after adding to the front: {q.peek()}")

print(f"Remove from the front of the deque: {q.removeFront  ()}")
print(f"Peek at the front element after dequeueing: {q.peek()}")

print(f"Remove from the back of the deque: {q.removeRear()}")
print(f"Peek at the front element after dequeueing: {q.peek()}")

print(f"Remove from the front of the deque: {q.removeFront  ()}")
print(f"Peek at the front element after dequeueing: {q.peek()}")

print(f"Is the queue empty? {q.is_empty()}")

print(f"Remove from the back of the deque: {q.removeRear()}")
print(f"Peek at the front element after dequeueing: {q.peek()}")

print(f"Is the queue empty? {q.is_empty()}")
print(f"Remove from the back of the deque: {q.removeRear()}")
print(f"Remove from the front of the deque: {q.removeFront  ()}")
print(f"Peek at the front element after dequeueing: {q.peek()}")

