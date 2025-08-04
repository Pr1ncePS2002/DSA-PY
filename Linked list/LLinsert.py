class Node():
    def __init__(self,value):
        self.data=value
        self.next=None
        
def print_l(head):
    temp=head
    while temp!=None:
        print(temp.data,end='->')
        temp=temp.next
    print()
    return 
def take_in():
    x=int(input("enter value:"))
    head=None
    tail=None
    while(x!=-1):
        newnode=Node(x)
        if head==None:
            head=newnode
            tail=newnode
        else:
            tail.next=newnode
            tail=newnode
        x=int(input("enter value:"))
    return head
def insert_head(head,data):
    newnode=Node(data)
    newnode.next=head
    head=newnode
    return head

def insert_tail(head,data):
    newnode=Node(data)
    if head is None:
        return newnode
    temp=head
    while temp.next!=None:
        temp=temp.next
    temp.next=newnode
    return head

def insert_index(head,data,index):
    if index==0 or head is None:
        return insert_index(head,data)
    newnode=Node(data)
    temp=head
    count=0
    while temp is not None and count< index-1:
        temp=temp.next 
        count+=1
    if temp is None:
        print("index out of bounds")
        return head 
    newnode.next=temp.next 
    temp.next=newnode
    return head 

def len_ll(head):
    temp=head
    ans=0
    while temp.next is not None:
        ans+=1
        temp=temp.next 
    return ans
        
head=take_in()
print_l(head)

            
                
            
        
        
        
        
        