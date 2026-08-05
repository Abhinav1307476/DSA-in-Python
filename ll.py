class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

class SinglyLinkedList:
    def __init__(self, head=None):
        self.head = head

    """ insert at beginning """
    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    """ insert at end """
    def insert_at_end(self, data):
        new_node = Node(data)
        # if the list is empty, make the new node the head
        if not self.head:
            self.head = new_node
            return
        # otherwise, traverse to the end of the list and append the new node
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    """ insert after an element """
    def insert_after_element(self, target_data, data):
        current = self.head
        while current:
            # if the current node's data matches the target data, insert the new node after it
            if current.data == target_data:
                new_node = Node(data)
                new_node.next = current.next
                current.next = new_node
                return
            # move to the next node in the list
            current = current.next
        raise ValueError("Element not found in the list")

    """ delete an element """
    def delete_element(self, target_data):
        current = self.head
        previous = None
        while current:
            # if the current node's data matches the target data, delete it
            if current.data == target_data:
                if previous is None:
                    # if the node to delete is the head, update the head to the next node
                    self.head = current.next
                else:
                    # otherwise, bypass the current node by linking the previous node to the next node
                    previous.next = current.next
                return
            # move to the next node in the list, keeping track of the previous node
            previous = current
            current = current.next
        raise ValueError("Element not found in the list")

    """ traverse """
    def traverse(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")


obj = SinglyLinkedList()

obj.insert_at_beginning(4)
obj.insert_at_beginning(3)
obj.insert_at_beginning(2)
obj.insert_at_beginning(1)

print("Initial linked list:")
obj.traverse()

obj.insert_at_end(6)
obj.insert_at_end(7)
print("Linked list after inserting at the end:")
obj.traverse()

obj.insert_after_element(4, 5)
obj.insert_after_element(7, 8)
print("Linked list after inserting after specific elements:")
obj.traverse()

obj.delete_element(1) # delete first element
obj.delete_element(5) # delete middle element
obj.delete_element(8) # delete last element
print("Linked list after deleting elements:")
obj.traverse()
