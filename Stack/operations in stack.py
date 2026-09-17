class stackUsingList:
    def __init__(self):
        self.__stack = []

    def push(self, data):
        self.__stack.append(data)
        print(f"pushed {data} into stack")

    def size(self):
        return len(self.__stack)

    def is_empty(self):
        if len(self.__stack) == 0:
            return True
        else:
            return False

    def top(self):
        if self.is_empty():
            print("stack is empty, no top element")
            return None
        else:
            return self.__stack[-1]

    def pop(self):
        if self.is_empty():
            print("stack is empty, no deletion can perform here")
            return None
        else:
            return self.__stack.pop()


my_stack = stackUsingList()

print(my_stack.is_empty())

(my_stack.push(10))
(my_stack.push(20))
(my_stack.push(30))
(my_stack.push(40))

(my_stack.pop())
(my_stack.is_empty())
(my_stack.top())