# What is an array ?
# What is a constructor ?
# arr = []
# # Singly LL
# class Node:
#     self.data = data
#     self.next = None
# # Doubly LL
# class Node:
#     self.data = data
#     self.next = None
#     self.prev = None
#
# # Circular Singly LL
# class Node:
#     self.data = data
#     self.next = head
#
# # Circular Doubly LL
# class Node:
#     self.data = data
#     # last node's next will point to head
#     self.next = head
#     # first node's prev will point to the last
#     self.prev = last

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None

    """Insert at the End of the List"""
    def insert_at_end(self, data):
        new_node = Node(data)
        # if head doesn't exist that means the LL is empty
        if self.head is None:
            self.head = new_node
            return
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    """Insert at the Beginning of the List"""
    def insert_at_beginning(self, data):
        new_node = Node(data)
        # no need to check if the beginning is None or not, If the head is none then, head will be replaced by the node
        new_node.next = self.head
        self.head = new_node

    """Insert after a node"""
    def insert_after(self, node_data, data):
        current = self.head
        while current:
            if current.data == node_data:
                new_node = Node(data)
                new_node.next = current.next
                current.next = new_node
                return
            current = current.next
        print("Element not found")

    """Delete an element from the List"""
    def delete(self, data):
        current = self.head
        previous = None
        while current:
            if current.data == data:
                if previous:
                    previous.next = current.next
                else:
                    self.head = current.next
                return
            previous = current
            current = current.next

    """Print the Linked List"""
    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")



ll = SinglyLinkedList()
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
