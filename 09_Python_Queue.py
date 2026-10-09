class Queue:
    def __init__(self):
        self.elements = []

    def is_empty(self):
        return len(self.elements) == 0

    def enqueue(self, item):
        self.elements.append(item) # append, inserts at the end of the list

    def dequeue(self):
        if self.is_empty():
            return
        else:
            return self.elements.pop(0)
    def peek(self):
        if self.is_empty():
            return
        return self.elements[0]


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
