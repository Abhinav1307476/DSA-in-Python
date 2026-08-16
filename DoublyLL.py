class Node:
    def __init__(self, data, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev

class DoublyLinkedList:
    def __init__(self, head=None):
        self.head = head

    """ insert at beginning """
    """
    Cases to be considered:
    1. If the list is empty, the new node becomes the head.
    2. If the list is not empty, the new node's next pointer should point to the current head, and the current head's previous pointer should point back to the new node. Finally, update the head to be the new node.
    """
    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        if self.head:
            self.head.prev = new_node
        self.head = new_node

    """ insert at end """
    """
    Cases to be considered:
    1. If the list is empty, the new node becomes the head.
    2. If the list is not empty, traverse to the end and insert the new node.
    """
    def insert_at_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node
        new_node.prev = current

    """ insert after an element """
    """
    Cases to be considered:
    1. If the target element is not found, raise a ValueError.
    2. If the target element is found at last position, the new node's next pointer should be None, and the current last node's next pointer should point to the new node.
    """
    def insert_after_element(self, target_data, data):
        current = self.head
        while current:
            if current.data == target_data:
                new_node = Node(data)
                new_node.next = current.next
                new_node.prev = current
                if current.next:
                    current.next.prev = new_node
                current.next = new_node
                return
            current = current.next
        raise ValueError("Element not found in the list")

    """ delete an element """
    """
    Cases to be considered:
    1. If the target element is not found, raise a ValueError.
    2. If the target element is the head, update the head to the next node.
    """
    def delete_element(self, target_data):
        current = self.head
        while current:
            if current.data == target_data:
                if current.prev:
                    current.prev.next = current.next
                else:
                    self.head = current.next  # Update head if needed
                if current.next:
                    current.next.prev = current.prev
                return
            current = current.next
        raise ValueError("Element not found in the list")

    """ traverse """
    def traverse(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

obj = DoublyLinkedList()

print("Initial linked list:")
obj.traverse()

print("Linked list after inserting at the beginning: 4")
obj.insert_at_beginning(4)
obj.traverse()

print("Linked list after inserting at the beginning: 3")
obj.insert_at_beginning(3)
obj.traverse()

print("Linked list after inserting at the beginning: 2")
obj.insert_at_beginning(2)
obj.traverse()

print("Linked list after inserting at the beginning: 1")
obj.insert_at_beginning(1)
obj.traverse()

print("Linked list after inserting at the end: 6")
obj.insert_at_end(6)
obj.traverse()

print("Linked list after inserting at the end: 7")
obj.insert_at_end(7)
obj.traverse()


print("Linked list after inserting after specific elements: 4 ->5")
obj.insert_after_element(4, 5)
obj.traverse()

print("Linked list after inserting after specific elements: 7 ->8")
obj.insert_after_element(7, 8)
obj.traverse()

print("Linked list after deleting first element")
obj.delete_element(1) # delete first element
obj.traverse()

print("Linked list after deleting middle element")
obj.delete_element(5) # delete middle element
obj.traverse()

print("Linked list after deleting last element")
obj.delete_element(8) # delete last element
obj.traverse()
