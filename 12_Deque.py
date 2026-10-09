class Deque:
    def __init__(self, capacity=5):
        self.capacity = capacity
        self.items = [None] * capacity
        self.front = -1
        self.rear = -1
        self.count = 0

    def is_empty(self):
        return self.count == 0

    def is_full(self):
        return self.count == self.capacity

    def addFront(self, item):
        if self.is_full():
            return "Deque is full"

        if self.is_empty():
            self.front = 0
            self.rear = 0
        else:
            self.front =  self.front - 1

        self.items[self.front] = item
        self.count += 1

    def addRear(self, item):
        if self.is_full():
            return "Deque is full"

        if self.is_empty():
            self.front = 0
            self.rear = 0
        else:
            self.rear = self.rear + 1

        self.items[self.rear] = item
        self.count += 1

    def removeFront(self):
        if self.is_empty():
            return "Deque is empty"

        item = self.items[self.front]
        self.items[self.front] = None
        self.count -= 1

        if self.is_empty():
            self.front = -1
            self.rear = -1
        else:
            self.front =  self.front + 1

        return item

    def removeRear(self):
        if self.is_empty():
            return "Deque is empty"

        item = self.items[self.rear]
        self.items[self.rear] = None
        self.count -= 1

        if self.is_empty():
            self.front = -1
            self.rear = -1
        else:
            self.rear = self.rear - 1

        return item

    def get_front(self):
        if self.is_empty():
            return "Deque is empty"
        return self.items[self.front]

    def get_rear(self):
        if self.is_empty():
            return "Deque is empty"
        return self.items[self.rear]

    def size(self):
        return self.count

    def __str__(self):
        return str(self.items)

    def peek(self):
        if self.is_empty():
            return
        return self.items[self.front]


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
