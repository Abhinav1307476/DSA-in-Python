class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class CircularDoublyLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            new_node.next = new_node
            new_node.prev = new_node
        else:
            last_node = self.head.prev
            # join last node's next and prev
            last_node.next = new_node
            # join the current node
            new_node.prev = last_node
            new_node.next = self.head
            # update head's prev
            self.head.prev = new_node

    def insert_at_beginning(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            new_node.next = new_node
            new_node.prev = new_node
        else:
            last_node = self.head.prev
            # join last node's next and prev
            last_node.next = new_node
            # join the current node
            new_node.prev = last_node
            new_node.next = self.head
            # update head's prev
            self.head.prev = new_node
            # update head to new node
            self.head = new_node

    def insert_after(self, target_data, data):
        if self.head is None:
            print("Linked List is empty")
            return
        current = self.head
        while True:
            if current.data == target_data:
                new_node = Node(data)
                # update the new node's next and prev
                new_node.next = current.next
                new_node.prev = current
                # tell current's next to point to new node
                current.next.prev = new_node
                current.next = new_node
                return
            current = current.next
            if current is self.head:
                break
        print("Target Data doesn't exist")

    def delete(self, target_data):
        # Case 1: If the list is empty
        if self.head is None:
            print("Linked List is empty")
            return
        # Case 2: If the list has only one node
        if self.head.data == target_data and self.head.next == self.head:
            self.head = None
            return
        # Case 3: If the list has more than one node
        current = self.head
        while True:
            if current.data == target_data:
                # update the next and prev of the surrounding nodes
                current.prev.next = current.next
                current.next.prev = current.prev
                # if we are deleting the head, update it
                if current == self.head:
                    self.head = current.next
                return
            current = current.next
            if current is self.head:
                break
        # Case 4: If the target data is not found in the list
        print("Target Data doesn't exist")

    def display(self):
        if self.head is None:
            print("Linked List is empty")
            return
        current = self.head
        while True:
            print(current.data, end=" <-> ")
            current = current.next
            if current is self.head:
                break
        print()


    def check_circularity(self):
        ctr = 0
        if self.head is None:
            print("Linked List is empty")
            return
        current = self.head
        while True:
            print(current.data, end=" <-> ")
            current = current.next
            if ctr >= 20:
                break
            ctr += 1
        print("")

ll = CircularDoublyLinkedList()
print("Initial LL")
ll.display()

print("LL after inserting at the end")
ll.insert_at_end(1)
ll.display()
ll.insert_at_end(2)
ll.display()
ll.insert_at_end(3)
ll.display()

print("LL after inserting at the beginning")
ll.insert_at_beginning(0)
ll.display()
ll.insert_at_beginning(-1)
ll.display()
ll.insert_at_beginning(-2)
ll.display()

# element not found
print("Insert after an element which doesn't exist")
ll.insert_after(10, 3)
ll.display()
print("Insert after an element which exists")
ll.insert_after(0, 0.5)
ll.display()
print("Insert after the last element")
ll.insert_after(3, 4)
ll.display()

print("Delete the first element")
ll.delete(-2)
ll.display()
print("Delete any middle element")
ll.delete(1)
ll.display()
print("Delete the last element")
ll.delete(4)
ll.display()
print("Delete an element which doesn't exist")
ll.delete(10)

ll.check_circularity()
