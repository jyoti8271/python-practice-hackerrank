#basic example
class Animal:
    def eat(self):
        print("Animal can eat")


class Dog(Animal):
    def bark(self):
        print("Dog can bark")


class Cat(Animal):
    def meow(self):
        print("Cat can meow")


d = Dog()
d.eat()
d.bark()

c = Cat()
c.eat()
c.meow()



#with constructor
class Animal:
    def __init__(self, name):
        self.name = name

    def show(self):
        print("Animal name:", self.name)


class Dog(Animal):
    def bark(self):
        print(self.name, "is barking")


class Cat(Animal):
    def meow(self):
        print(self.name, "is meowing")


d = Dog("Tommy")
d.show()
d.bark()

c = Cat("Kitty")
c.show()
c.meow()



#child class has own constructor 
class Animal:
    def __init__(self, name):
        self.name = name


class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed

    def show(self):
        print(self.name, self.breed)


class Cat(Animal):
    def __init__(self, name, color):
        super().__init__(name)
        self.color = color

    def show(self):
        print(self.name, self.color)


d = Dog("Tommy", "German Shepherd")
d.show()

c = Cat("Kitty", "White")
c.show()


##method overriding
class Animal:
    def sound(self):
        print("Animal makes sound")


class Dog(Animal):
    def sound(self):
        print("Dog barks")


class Cat(Animal):
    def sound(self):
        print("Cat meows")


d = Dog()
d.sound()

c = Cat()
c.sound()

# real world examples
class Employee:
    def work(self):
        print("Employee is working")


class Developer(Employee):
    def coding(self):
        print("Developer is coding")


class Tester(Employee):
    def testing(self):
        print("Tester is testing")


class Manager(Employee):
    def managing(self):
        print("Manager is managing")


d = Developer()
d.work()
d.coding()

t = Tester()
t.work()
t.testing()

m = Manager()
m.work()
m.managing()

#hiererchical +polymorphism
class Employee:
    def work(self):
        print("Employee working")


class Developer(Employee):
    def work(self):
        print("Developer writing code")


class Tester(Employee):
    def work(self):
        print("Tester testing software")


class Manager(Employee):
    def work(self):
        print("Manager managing team")


employees = [Developer(), Tester(), Manager()]

for employee in employees:
    employee.work()
    
    
#abstaract classa advance exaple
from abc import ABC, abstractmethod


class Employee(ABC):

    @abstractmethod
    def work(self):
        pass


class Developer(Employee):

    def work(self):
        print("Developer writes code")


class Tester(Employee):

    def work(self):
        print("Tester tests software")


class Designer(Employee):

    def work(self):
        print("Designer creates UI")


employees = [Developer(), Tester(), Designer()]

for employee in employees:
    employee.work()