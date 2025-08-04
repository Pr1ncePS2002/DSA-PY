from collections import deque
from PrintTree import *

def take_input():
    data=int(input("enter value:"))
    node=Tree(data)
    num_children=int(input(f"enter no of children for {data}:"))
    for _ in range(num_children):
        child=take_input()
        node.child.append(child)
    return 

def input_better():
    data=int(input("enter root:"))
    root=Tree(data)
    
    queue=deque([root])
    while len(queue)!=0:
        current=queue.popleft()
        num_child=int(input("enter the no of children for "+str(current.data) +":"))
        for i in range(num_child):
            child_data=int(input(f"enter data for child {i+1}  of node {current.data}: "))
            child_node=Tree(child_data)
            current.child.append(child_node)
            queue.append(child_node)
    return root    
root=input_better()
print_tree(root)