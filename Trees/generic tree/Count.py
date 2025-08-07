from PrintTree import *
from TakeInput import input_better

def count_node(root):
    if root==None:
        return 0
    num_nodes=1
    for eachchild in root.children:
        num_nodes=num_nodes+count_node(eachchild)
    return num_nodes

def count_better(root):
    if root is None:
        return 0
    count = 1  # Count the current node
    for child in root.children:
        count += count_node(child)

    return count
   
root=input_better()
print(count_node(root))
