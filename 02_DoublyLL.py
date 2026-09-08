class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    """ Insert at the beginning of the list """
    """
    Case 1: if the is not empty, existing head's prev will point to new_node
    """
    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        if self.head:
            self.head.prev = new_node
        self.head = new_node

    """ Insert at the end of the list """
    """
    Case 1: If the list is empty, just assign the new_node to head
    Case 2: Else, Traverse, last node's next will be new_node and new_node.prev will be last node
    """
    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return

        curr_node = self.head
        while curr_node.next:
            curr_node = curr_node.next
        curr_node.next = new_node
        new_node.prev = curr_node

    """ Insert after an element """
    """
    1. node.prev. = current
    2. node.next = current.next
    3. current.next.prev = node
    4. current.next = node
    """
    def insert_after(self, node_data, data):
        curr_node = self.head
        while curr_node:
            if curr_node.data == node_data:
                new_node = Node(data)
                new_node.prev = curr_node
                new_node.next = curr_node.next
                if curr_node.next:
                    curr_node.next.prev = new_node
                curr_node.next = new_node
                return
            curr_node = curr_node.next
        print("Element not found")

    """ Delete an item from the list """
    """
    1st 1st
    head = head.next
    head.prev = None
    2nd middle
    current.prev.next = currnent.next
    current.next.prev = current.prev
    3rd end
    current.prev.next = currnent.next
    """
    def delete(self, data):
        curr_node = self.head
        while curr_node:
            if curr_node.data == data:
                if curr_node.prev is None:
                    self.head = curr_node.next
                else:
                    curr_node.prev.next = curr_node.next

                if curr_node.next:
                    curr_node.next.prev = curr_node.prev
                return
            curr_node = curr_node.next
        print("Element not found")

    """Print the Linked List"""
    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")


ll = DoublyLinkedList()
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

print("Delete the first element")
ll.delete(-2)
ll.display()
print("Delete any middle element")
ll.delete(1)
ll.display()
print("Delete the last element")
ll.delete(3)
ll.display()
print("Delete a non-existent element")
ll.delete(100)
ll.display()


