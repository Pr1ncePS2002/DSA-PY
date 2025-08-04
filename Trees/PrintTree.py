class Tree():
    def __init__(self,data):
        self.data=data
        self.children=[]

def print_tree(root):
    if (root==None):
        return None
    print(root.data,end=":")
    for i in root.children:
        print(i.data,end=",")
    print()
    for i in root.children:
        print_tree(i)
        