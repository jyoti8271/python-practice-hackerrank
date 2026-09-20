class Node:
    def __init__(self, value):
        self.data = value       
        self.next = None


def print_LL(head):
    temp = head
    while temp != None:
        print(temp.data, end=" -> ")
        temp = temp.next        
    print("None")


def take_input():
    value = int(input("Enter the number to stop -1 "))
    head = None
    
    while value != -1:
        newnode = Node(value)
        
        if head is None:
            head = newnode
        else:
            temp = head
            while temp.next != None:
                temp = temp.next
            temp.next = newnode  
            
        value = int(input("Enter the number (-1 to stop): "))  
        
    return head



head = take_input()
print("\n Linked List:")
print_LL(head)