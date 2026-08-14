# a = 10
# b = 10

# s = {a, b}
# print(s)


class Student:
    #constructor
    def __init__(self, name, age):
    
    #instance method
        self.name = name
        self.age = age
        
    #object creation

s1 = Student("jyoti", 20)
s2 = Student("jyoti", 20)

s={s1,s2}

print(s1.name)
print(s2.name)
print(len(s))


# using list
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

s1 = Student("Rahul", 20)
s2 = Student("Rahul", 20)

lst = [s1, s2]

print(len(lst))




