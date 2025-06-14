from LL2 import *

head=take_input1()
print_ll(head)

# INSERT AT HEAD
def insert_at_head(head,data):
    newnode=Node(data)
    newnode.next=head
    head=newnode
    return head

# head=insert_at_head(head,100)
# print_ll(head)

# INSERT AT TAIL
def insert_at_tail(head,data):
    newnode=Node(data)
    if head is None:
        return newnode
    temp=head 
    while temp.next!=None:
        temp=temp.next
    temp.next=newnode
    return head  
# head=insert_at_tail(head,100)
# print_ll(head)
    
