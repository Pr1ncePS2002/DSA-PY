class Tree():
    def __init__(self,data):
        self.data=data
        self.child=[]

def print_tree(root):
    if (root==None):
        return None
    print(root.data,end=":")
    for i in root.child:
        print(i.data,end=",")
    print()
    for i in root.child:
        print_tree(i)
        