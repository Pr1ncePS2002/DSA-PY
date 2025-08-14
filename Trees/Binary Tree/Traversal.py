from PrintTree import *
from collections import deque
from TakeInput import input_better

#PRE-ORDER TRAVERSAL

def preorder(root):
    if root is None:
        return 
    print(root.data,end=" ")
    preorder(root.left)
    preorder(root.right)
# root=input_better()
# print(preorder(root))    

#POSTORDER TRAVERSAL

def postorder(root):
    if root is None:
        return 
    postorder(root.left)
    postorder(root.right)
    print(root.data,end=" ")
    
#IN ORDER TRAVERSAL
def inorder(root):
    if root is None:
        return 
    inorder(root.left)
    print(root.data,end=" ")
    inorder(root.right)
    
    

