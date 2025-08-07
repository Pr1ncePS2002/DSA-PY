from TakeInput import take_input
def height_tree(root):
    if root==None:
        return 0
    height=1
    max_height=0
    for eachchild in root.children:
        max_height=max(max_height,height_tree(eachchild))
    height=height+max_height
    return height

def height_better(root):
    if root is None:
        return 0

    max_child_height = 0
    for child in root.children:
        child_height = height_tree(child)
        if child_height > max_child_height:
            max_child_height = child_height

    return 1 + max_child_height
root=take_input()
print(height_better(root))
