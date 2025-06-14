from LL2 import *
#INSERT AT TAIL
head=take_input1()
print_ll(head)
def insert_at_tail_recursive(head, data):
    if head==None:
        return Node(data)
    head.next= insert_at_tail_recursive(head.next,data)
    return head
        

# head=insert_at_tail_recursive(head,100)
# print_ll(head)
