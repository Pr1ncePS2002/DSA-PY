from PrintTree import *
from collections import deque
def take_input():
    data=int(input("Enter the data for the tree:"))
    if data==-1:
        return 
    node=BinaryTree(data)
    print(f"enter the left child of {data}")
    node.left=take_input()
    print(f"enter the right child of {data}")
    node.right=take_input()
    
    return node

def input_better():
    data=int(input("Enter the data for the tree:"))
    if data==-1:
        return 
    root=BinaryTree(data)
    queue=deque([root])
    
    while len(queue)!=0:
        curr=queue.popleft()
        
        left_child=int(input(f"enter left child for {curr.data}:"))
        if left_child!=-1:
            left_node=BinaryTree(left_child)
            curr.left=left_node
            queue.append(left_node)
            
        right_child=int(input(f"enter right child for {curr.data}:"))
        if right_child!=-1:
            right_node=BinaryTree(right_child)
            curr.right=right_node
            queue.append(right_node)
    return root

root=input_better()
print(print_binary(root))