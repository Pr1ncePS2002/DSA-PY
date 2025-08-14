from TakeInput import input_better

def height(root):
    if root is None:
        return 0
    left_node=height(root.left)
    right_node=height(root.right)
    
    heightTree= 1+max(left_node,right_node)
    return heightTree

def diameterTree(root):
    if root is None:
        return 0,0
    
    leftheight,leftdiameter=diameterTree(root.left)
    rightheight,rightdiameter=diameterTree(root.right)
    
    diameter_through_root=leftheight+rightheight
    
    ans=max(diameter_through_root,leftdiameter,rightdiameter)
    current_height= 1+ max(leftheight,rightheight)
    
    return current_height,ans

    
    