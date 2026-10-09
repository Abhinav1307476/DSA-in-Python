class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def insert(root, value):
    if root is None:
        return Node(value)
    if value < root.data:
        root.left = insert(root.left, value)
    elif value > root.data:
        root.right = insert(root.right, value)
    return root

def search(root, value):
    if root is None or root.data == value:
        return root
    if value < root.data:
        return search(root.left, value)
    return search(root.right, value)

def in_order_traversal(root):
    if root:
        in_order_traversal(root.left)
        print(root.data, end=' ')
        in_order_traversal(root.right)

def in_order_successor(current):
    current = current.right
    while current.left:
        current = current.left
    return current

def in_order_predecessor(current):
    current = current.left
    while current.right:
        current = current.right
    return current

def delete(root, value):
    if root is None:
        return root
    # find the node to be deleted
    if value < root.data:
        root.left = delete(root.left, value)
    elif value > root.data:
        root.right = delete(root.right, value)
    # else part represent the item is found on current node
    else:
        # case: if only right child or no child
        if root.left is None:
            return root.right
        # case: if only left child or no child
        elif root.right is None:
            return root.left
        # case: if both children exist
        else:
            successor = in_order_successor(root)
            root.data = successor.data # overwrite root's data to the successor's data
            root.right = delete(root.right, successor.data) # call delete with right subtree, and value as successor's data
    return root

root = insert(None, 10)
root = insert(root, 5)
root = insert(root, 15)
root = insert(root, 3)
root = insert(root, 7)
root = insert(root, 12)
root = insert(root, 18)
root = insert(root, 1)
root = insert(root, 5)
in_order_traversal(root)
print()

if search(root, 700):
    print("\nValue found in the BST.")
else:
    print("\nValue not found in the BST.")

# check successor and predecessor
print("In-order predecessor of root:", in_order_predecessor(root).data)
print("In-order successor of root:", in_order_successor(root).data)

# case: delete item doesn't exist
root = delete(root, 100)
in_order_traversal(root)
print()
# case: delete item with no child
root = delete(root, 1)
in_order_traversal(root)
print()
# case: delete item with one child
# root = delete(root, 3)
# in_order_traversal(root)
# print()
# case: delete item with two children
# root = delete(root, 5)
# in_order_traversal(root)
# print()
# case: delete root
# root = delete(root, 10)
# in_order_traversal(root)
# print()




