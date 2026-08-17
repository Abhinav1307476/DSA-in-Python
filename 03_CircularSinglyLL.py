class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularSinglyLinkedList:
    def __init__(self):
        self.head = None

    """ insert at beginning """
    def insert_at_beginning(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            new_node.next = self.head  # Points to itself for a single-node circular list
        else:
            current = self.head
            # Traverse to the last node
            while current.next != self.head:
                current = current.next
            current.next = new_node  # Last node points to new_node
            new_node.next = self.head  # New node points to old head
            self.head = new_node      # Head is updated to new_node

    """ insert at end """
    def insert_at_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            new_node.next = self.head
        else:
            current = self.head
            # Traverse to the last node
            while current.next != self.head:
                current = current.next
            current.next = new_node  # Last node points to new_node
            new_node.next = self.head  # New node points to head

    """ insert after an element """
    def insert_after_element(self, target_data, data):
        if not self.head:
            raise ValueError("List is empty. Cannot insert after element.")

        current = self.head
        # Iterate at least once because it's circular
        while True:
            if current.data == target_data:
                new_node = Node(data)
                new_node.next = current.next
                current.next = new_node
                return
            current = current.next
            if current == self.head: # If we've circled back to head, element not found
                break
        raise ValueError(f"Element '{target_data}' not found in the list")

    """ delete an element """
    def delete_element(self, target_data):
        if not self.head:
            raise ValueError("List is empty. Cannot delete from an empty list.")

        current = self.head
        previous = None

        # Case 1: Deleting the only node
        if self.head.data == target_data and self.head.next == self.head:
            self.head = None
            return

        # Case 2: Deleting the head node (when there are multiple nodes)
        if self.head.data == target_data:
            # Find the last node
            while current.next != self.head:
                current = current.next
            current.next = self.head.next # Last node points to new head
            self.head = self.head.next    # Update head
            return

        # Case 3: Deleting a node other than the head
        while current.next != self.head: # Iterate until before head (to check all nodes)
            previous = current
            current = current.next
            if current.data == target_data:
                previous.next = current.next
                return

        # Case 4: Target data is the last node before circling back to head, but not head itself
        # This is implicitly handled by the loop if previous is assigned correctly
        # and current.next != self.head is the loop condition.
        # If the target_data is the last node and not the head, previous.next should skip it.
        # The loop condition current.next != self.head handles finding the last node if target_data is not found
        # before the last iteration.

        raise ValueError(f"Element '{target_data}' not found in the list")


    """ traverse """
    def traverse(self):
        if not self.head:
            print("List is empty")
            return

        current = self.head
        elements = []
        while True:
            elements.append(str(current.data))
            current = current.next
            if current == self.head:
                break
        print(" -> ".join(elements) + " -> (back to head)")


# Example Usage
obj = CircularSinglyLinkedList()

print("Initial circular linked list:")
obj.traverse()

print("\n--- Inserting elements ---")
print("Inserting 4 at beginning:")
obj.insert_at_beginning(4)
obj.traverse()

print("Inserting 3 at beginning:")
obj.insert_at_beginning(3)
obj.traverse()

print("Inserting 2 at beginning:")
obj.insert_at_beginning(2)
obj.traverse()

print("Inserting 1 at beginning:")
obj.insert_at_beginning(1)
obj.traverse()

print("Inserting 6 at end:")
obj.insert_at_end(6)
obj.traverse()

print("Inserting 7 at end:")
obj.insert_at_end(7)
obj.traverse()

print("\n--- Inserting after specific elements ---")
print("Inserting 5 after 4:")
obj.insert_after_element(4, 5)
obj.traverse()

print("Inserting 8 after 7:")
obj.insert_after_element(7, 8)
obj.traverse()

print("\n--- Deleting elements ---")
print("Deleting 1 (head element):")
obj.delete_element(1) # delete head element
obj.traverse()

print("Deleting 5 (middle element):")
obj.delete_element(5) # delete middle element
obj.traverse()

print("Deleting 8 (last element):")
obj.delete_element(8) # delete last element
obj.traverse()

print("Deleting 3 (remaining element, testing single node deletion edge case):")
obj.delete_element(3)
obj.traverse()

print("Deleting 2 (remaining element, testing single node deletion edge case):")
obj.delete_element(2)
obj.traverse()

print("Deleting 4 (remaining element, testing single node deletion edge case):")
obj.delete_element(4)
obj.traverse()

print("Deleting 6 (remaining element, testing single node deletion edge case):")
obj.delete_element(6)
obj.traverse()

print("Deleting 7 (remaining element, testing single node deletion edge case):")
obj.delete_element(7)
obj.traverse()

print("\nTrying to delete from an empty list:")
try:
    obj.delete_element(10)
except ValueError as e:
    print(e)

print("\nTrying to insert after an element in an empty list:")
try:
    obj.insert_after_element(10, 11)
except ValueError as e:
    print(e)
