class Node:
    def __init__(self,value):
        self.data=value
        self.next=None
        
def print_ll(head):
    temp=head
    while temp!=None:
        print(temp.data,end="->")
        temp=temp.next
    print()
    return
                 
                 
def take_input1():
    x=int(input("enter number:"))
    head1=None
    tail=None
    
    while (x!=-1):
        newnode1=Node(x)
        if head1==None:
            head1=newnode1
            tail=newnode1
        else:
            tail.next=newnode1
            tail=newnode1
        x=int(input("enter value:"))
    return head1
newhead=take_input1()
print_ll(newhead)
    
        