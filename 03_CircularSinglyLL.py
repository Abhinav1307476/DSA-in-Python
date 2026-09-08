class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularSinglyLinkedList:
    def __init__(self):
        self.head = None

    """Insert at the End of the List"""
    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next is not self.head:
                current = current.next
            current.next = new_node
        # in both cases we need to attach the head to new node's next
        new_node.next = self.head

    """Insert at the Beginning of the List"""
    def insert_at_beginning(self, data):
        new_node = Node(data)
        if self.head is None:
            new_node.next = new_node
        else:
            new_node.next = self.head
            current = self.head
            while current.next is not self.head:
                current = current.next
            current.next = new_node
        self.head = new_node

    """ Insert after an element """
    def insert_after(self, target_data, data):
        if self.head is None:
            print("Linked List is empty")
            return
        current = self.head
        while True:
            if current.data == target_data:
                new_node = Node(data)
                new_node.next = current.next
                current.next = new_node
                return
            current = current.next
            if current is self.head:
                break
        print("Target Data doesnt exist")

    """Print the Linked List"""
    def display(self):
        if self.head is None:
            print("Linked List is empty")
            return
        current = self.head
        while True:
            print(current.data, end=" -> ")
            current = current.next
            if current is self.head:
                break
        print("")

    """Delete an element from the List"""
    def delete(self, data):
        # Case1: if the LL is empty
        if self.head is None:
            print("Linked List is empty")
            return

        # Case2: If the length is one and item exits
        if self.head.data == data and self.head.next is self.head:
            self.head = Node
            return
        current = self.head
        previous = None
        #Case3: Delete the head where there are other Nodes
        if self.head.data == data:
            while current.next is not self.head:
                current = current.next
            current.next = self.head.next
            self.head = self.head.next
            return

        #Case4: deleting a node other than the 1st node
        while True:
            if current.data == data:
                previous.next = current.next
                return
            previous = current
            current = current.next
            if current is self.head:
                break
        print("Element not found")
           
    """Verify Circular linked list"""
    def check_circularity(self):
        ctr = 0
        if self.head is None:
            print("Linked List is empty")
            return
        current = self.head
        while True:
            print(current.data, end=" -> ")
            current = current.next
            if ctr >= 20:
                break
            ctr += 1
        print("")


ll = CircularSinglyLinkedList()
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
