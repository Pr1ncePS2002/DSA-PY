from LLinsert import *
def search_val(head,value):
    temp=head
    index=0
    while temp is not None:
        if (temp.data==value):
            return index
        temp=temp.next 
        index+=1
    return "Not found"
def search_index(head,index):
    if head is None or index<0:
        return None
    temp=head
    count=0
    while temp is not None:
        if count==index:
            return temp.data
        count+=1
        temp=temp.next
    return None
print("searching")

print(search_index(head,3))