from LL2 import *

def lenll(head):
    temp=head
    ans=0
    while temp:
        ans=ans+1
        temp=temp.next 
    return ans

headofll=take_input1()
lengthofll=lenll(headofll)
print(lengthofll)


