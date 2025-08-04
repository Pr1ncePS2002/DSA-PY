class Node():
    def __init__(self,value):
        self.data=value
        self.next=None
class StackLL:
    def __init__(self):
        self.head=None
        self.size=0
    def push(self,data):
        newnode=Node(data)
        self.size+=1
        if self.head is None:
            self.head=newnode
            return f"added {data} to stack"
        newnode.next=self.head
        self.head=newnode
        return f"added {data} to stack"
    
    def top(self):
        if self.head is None or self.size==0:
            return f"stack is empty"
        return self.head.data
    
    def pop(self):
        if self.head is None or self.size==0:
            return f"stack is empty"
        topdata=self.head.data
        self.head=self.head.next
        self.size-=1
        return topdata
    
    def get_size(self):
        return self.size
    def is_empty(self):
        return self.size==0
    
mystack=StackLL()
print(mystack.is_empty())
print(mystack.push(10))
print(mystack.push(20))
print(mystack.push(30))
print(mystack.push(40))
print(mystack.is_empty())
print(mystack.pop())
print(mystack.top())
print(mystack.get_size())



        