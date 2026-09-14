class Queue:
    def __init__(self):
        self.size = 5
        self.items = [None] * self.size
        self.front = -1
        self.rear = -1

    def is_empty(self):
        return self.front == -1

    def is_full(self):
        return self.rear + 1 == self.size 

    def enqueue(self, item):
        if self.is_full():
            print("***Queue is full. Cannot enqueue item.***")
            return
        self.rear = self.rear + 1
        self.items[self.rear] = item
        if self.front == -1:
            self.front = 0

    def dequeue(self):
        if self.is_empty():
            return "Queue is empty" 
        item = self.items[self.front]
        if self.front == self.rear:
            self.front = -1
            self.rear = -1
        else:
            self.front = self.front + 1
        return item

    def peek(self):
        if self.is_empty():
            return "Queue is empty"
        else:
            return self.items[self.front]

    def size(self):
        if self.is_empty():
            return 0
        else:
            return self.rear - self.front + 1

q = Queue()
print(f"Is the queue empty? {q.is_empty()}")
print(f"Dequeue from the queue: {q.dequeue()}")  # This will print a message since the queue is empty
q.enqueue(10)
print(f"Peek at the front element after enqueueing 10: {q.peek()}")
q.enqueue(20)
print(f"Peek at the front element after enqueueing 20: {q.peek()}")
q.enqueue(30)
print(f"Peek at the front element after enqueueing 30: {q.peek()}")

print(f"Dequeue from the queue: {q.dequeue()}")
print(f"Peek at the front element after dequeueing: {q.peek()}")

print(f"Dequeue from the queue: {q.dequeue()}")
print(f"Peek at the front element after dequeueing: {q.peek()}")


print(f"Is the queue empty? {q.is_empty()}")

print(f"Dequeue from the queue: {q.dequeue()}")
print(f"Peek at the front element after dequeueing: {q.peek()}")

print(f"Is the queue empty? {q.is_empty()}")
print(f"Dequeue from the queue: {q.dequeue()}")