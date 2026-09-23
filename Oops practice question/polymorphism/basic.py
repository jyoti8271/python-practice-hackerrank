#method overriding
class animal:
    def sound(self):
        print("animal makes sound")
        
class dog(animal):
    def sound(self):
        print("dog barks")
        
class cat(animal):
    def sound(self):
        print("cat meows")
        
        
dog1=dog()
cat1=cat()
dog1.sound()
cat1.sound()


##polymorphism with function ---> one function work with different object

class dog:
    def sound(self):
        print("bark")
        
class cat:
    def sound(self):
        print("meow")
        
def make_sound(animal):
    animal.sound()
    
dog2=dog()
cat2=cat()

make_sound(dog)
make_sound(cat)



##duck typing---->
class Dog:
    def sound(self):
        print("Bark")


class Cat:
    def sound(self):
        print("Meow")


class Cow:
    def sound(self):
        print("Moo")


def make_sound(animal):
    animal.sound()


make_sound(Dog())
make_sound(Cat())
make_sound(Cow())


##operator overloading
print(10+20)
print("hello"+"world")
print([1,2]+[3,4])


##custom operator overloading

class point:
    def __init__(self,x,y):
        self.x=x
        self.y=y
        
    def __add__(self,other):
        return point(self.x+other.x,self.y+other.y)
    
p1=point(10,20)
p2=point(6,10)

p3=p1+p2
print(p3.x)
print(p3.y)




class student:
    def __init__(self,marks):
        self.marks=marks
    
    def __gt__(self,other):
        return self.marks>other.marks
    
s1=student(80)
s2=student(70)

print(s1>s2)