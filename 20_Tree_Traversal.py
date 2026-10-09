class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def pre_order_traversal(root):
    if root:
        print(root.data, end=' ')
        pre_order_traversal(root.left)
        pre_order_traversal(root.right)

def post_order_traversal(root):
    if root:
        post_order_traversal(root.left)
        post_order_traversal(root.right)
        print(root.data, end=' ')

def in_order_traversal(root):
    if root:
        in_order_traversal(root.left)
        print(root.data, end=' ')
        in_order_traversal(root.right)

root = Node(1)
root.left = Node(3)
root.right = Node(4)
root.left.left = Node(9)
root.left.right = Node(12)
root.right.left = Node(17)
root.right.right = Node(18)

pre_order_traversal(root)
print()  # For better readability
post_order_traversal(root)
print()  # For better readability
in_order_traversal(root)