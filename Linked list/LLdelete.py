from LLinsert import *

def delete_head(head):
    if head is None:
        return None
    newhead=head.next #new head points to next node
    return newhead

def is_tail(node):
    if node==None:
        return True
    if node.next==None:
        return True
    return False

def delete_tail(head):
    if head is None or head.next==None:
        return None 
    temp=head
    while temp.next.next is not None:
        temp=temp.next 
    temp.next=None
    return head

def delete_index(head,index):
    if head is None:
        return None
    if index==0:
        head=head.next 
    temp=head
    count=0
    while temp is not None and count<index-1:
        temp=temp.next 
        count+=1
    if temp is None or temp.next is None:
        print("index out of bounds")
    temp.next=temp.next.next 
    return head

def delete_value(head,value):
    if head is None:
        return None
    if head.data==value:
        head=head.next 
    temp=head
    while temp.next is not None and temp.next.data!=value:
        temp=temp.next 
    if temp.next is None:
        print("not found")
        return head
    temp.next=temp.next.next
    return head
    
    


head =delete_value(head,30)
print("after deletion")
print_l(head)
    


