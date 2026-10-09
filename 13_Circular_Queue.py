class Circular_Queue:
    def __init__(self, size):
        self.size = size
        self.queue = [None] * size
        self.front = self.rear = -1

    def is_full(self):
        return (self.rear + 1) % self.size == self.front

    def is_empty(self):
        return self.front == -1

    def enqueue(self, item):
        if self.is_full():
            print("Queue is full")
            return
        if self.front == -1:
            self.front = 0
        self.rear = (self.rear + 1) % self.size
        self.queue[self.rear] = item

    def dequeue(self):
        if self.is_empty():
            return None
        item = self.queue[self.front]
        if self.front == self.rear:
            # Queue has only one element, reset to empty state
            self.front = self.rear = -1
        else:
            self.front = (self.front + 1) % self.size
        return item

    def peek(self):
        if self.is_empty():
            return None
        return self.queue[self.front]

    def check_circularity(self):
        ctr = self.front
        while True:
            print(self.queue[(ctr% self.size)], end="->")
            ctr = ctr + 1
            if ctr == 20:
                break
        print()
        

cq = Circular_Queue(5)

# Empty tests
print(f"Is the queue empty? {cq.is_empty()}")
print(f"Is the queue full? {cq.is_full()}")
print("Peeking at the front element:", cq.peek())
print("Dequeuing from the empty queue:", cq.dequeue())

# Enqueue tests
cq.enqueue(10)
print("Peeking at the front element:", cq.peek())
print(f"Is the queue empty? {cq.is_empty()}")
print(f"Is the queue full? {cq.is_full()}")

print("Dequeuing from the queue:", cq.dequeue())
print("Peeking at the front element:", cq.peek())
cq.enqueue(10)
print("Peeking at the front element:", cq.peek())
cq.enqueue(20)
print("Peeking at the front element:", cq.peek())
cq.enqueue(30)  
print("Peeking at the front element:", cq.peek())
cq.enqueue(40)
print("Peeking at the front element:", cq.peek())
print(f"Is the queue full? {cq.is_full()}")
cq.enqueue(50)  # This should indicate that the queue is full
print("Peeking at the front element:", cq.peek())
print(f"Is the queue full? {cq.is_full()}")
cq.enqueue(60)  # This should indicate that the queue is full
cq.check_circularity()

print("Dequeuing from the queue:", cq.dequeue())
cq.enqueue(60)
print(f"Is the queue full? {cq.is_full()}")
cq.check_circularity()

print("Peeking at the front element:", cq.peek())
print("Dequeuing from the queue:", cq.dequeue())

print("Peeking at the front element:", cq.peek())
print("Dequeuing from the queue:", cq.dequeue())

print("Peeking at the front element:", cq.peek())
print("Dequeuing from the queue:", cq.dequeue())

print("Peeking at the front element:", cq.peek())
print("Dequeuing from the queue:", cq.dequeue())
print(f"Is the queue empty? {cq.is_empty()}")

print("Peeking at the front element:", cq.peek())
print("Dequeuing from the queue:", cq.dequeue())
print(f"Is the queue empty? {cq.is_empty()}")

print("Dequeuing from the queue:", cq.dequeue())



