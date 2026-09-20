class Node:
    def __init__(self,value):
        self.data=value
        self.next=None
        
first=Node(1)
second=Node(2)
Third=Node(3)

print(id,(first),id(second),id(Third))

first.next=second
second.next=Third


head= first
print(head.data)
print(head.next.data)
print(head.next.next.data)
