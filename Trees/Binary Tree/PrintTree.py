class BinaryTree:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
    
root=BinaryTree(1)
root.left=BinaryTree(2)
root.right=BinaryTree(3)

def print_binary(root):
    if root is None:
        return
    print(root.data,end=":")
    
    if root.left is not None:
        print(f"L->{root.left.data}",end=", ")
    else:
        print("L->none",end=",")
        
    if root.right is not None:
        print(f"R->{root.right.data}",end=",")
    else:
        print("R->none",end=",")
    print()
        
    print_binary(root.left)
    print_binary(root.right)
    
# print_binary(root)
