class Node:
    def __init__(self, value):
        self.data = value
        self.next = None


def print_LL(head):
    temp = head
    while temp is not None:
        print(temp.data, end=" -> ")
        temp = temp.next
    print("None")


def take_input_better():
    value = int(input("Enter value (-1 to stop): "))
    head = None
    tail = None
    
    while value != -1:
        newNode = Node(value)
        
        
        if head is None:
            head = newNode
            tail = newNode
        else:
            tail.next = newNode
            tail = newNode
            
            
        
        value = int(input("Enter value (-1 to stop): "))
    
    return head

new_head = take_input_better() 
print("\n Linked List:")
print_LL(new_head)



########using without -1
# def take_input_by_count():
#     n = int(input("Kitne nodes daalne hain? : "))
#     head = None
#     tail = None
    
#     for i in range(n):
#         value = int(input(f"Node {i+1} ki value: "))
#         newNode = Node(value)
        
#         if head is None:
#             head = newNode
#             tail = newNode
#         else:
#             tail.next = newNode
#             tail = newNode
            
#     return head