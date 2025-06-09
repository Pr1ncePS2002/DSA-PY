class Node:
    def __init__(self,value):
        self.data=value
        self.next=None

def lenll(head):
    temp=head
    ans=0
    while temp:
        ans=ans+1
        temp=temp.next 
    return ans
                                  
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

headofll=take_input1()
lengthofll=lenll(headofll)
print(headofll)
print(lengthofll)

