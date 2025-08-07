def preorder_traversal(root):
    if root is None:
        return
    
    print(root.data, end=" ")  # Visit root
    for child in root.children:
        preorder_traversal(child)  # Visit each subtree

def postorder_traversal(root):
    if root is None:
        return
    
    for child in root.children:
        postorder_traversal(child)
    print(root.data, end=" ")  # Visit root after children

from collections import deque

def level_order_traversal(root):
    if root is None:
        return

    queue = deque([root])
    while queue:
        current = queue.popleft()
        print(current.data, end=" ")

        for child in current.children:
            queue.append(child)
