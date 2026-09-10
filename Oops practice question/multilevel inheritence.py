#1, basic multilevel question
class Animal:
    def eat(self):
        print("Animal is eating")


class Dog(Animal):
    def bark(self):
        print("Dog is barking")


class Puppy(Dog):
    def play(self):
        print("Puppy is playing")


puppy1 = Puppy()

puppy1.eat()
puppy1.bark()
puppy1.play()


#2.multilvel inheritence throught constructor
class Person:
    def __init__(self, name):
        self.name = name


class Student(Person):
    def __init__(self, name, roll_no):
        super().__init__(name)
        self.roll_no = roll_no


class CollegeStudent(Student):
    def __init__(self, name, roll_no, branch):
        super().__init__(name, roll_no)
        self.branch = branch


student1 = CollegeStudent("Jyoti", 101, "Computer Science")

print("Name:", student1.name)
print("Roll No:", student1.roll_no)
print("Branch:", student1.branch)


#3.vheicle->car->tesla
class Vehicle:
    def __init__(self, brand):
        self.brand = brand


class Car(Vehicle):
    def __init__(self, brand, model):
        super().__init__(brand)
        self.model = model


class Tesla(Car):
    def __init__(self, brand, model, battery):
        super().__init__(brand, model)
        self.battery = battery


tesla1 = Tesla("Tesla", "Model 3", "75 kWh")

print("Brand:", tesla1.brand)
print("Model:", tesla1.model)
print("Battery:", tesla1.battery)

#4.employee-developer-senior developer
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary


class Developer(Employee):
    def __init__(self, name, salary, language):
        super().__init__(name, salary)
        self.language = language


class SeniorDeveloper(Developer):
    def __init__(self, name, salary, language, experience):
        super().__init__(name, salary, language)
        self.experience = experience


dev = SeniorDeveloper("Rahul", 60000, "Python", 5)

print("Name:", dev.name)
print("Salary:", dev.salary)
print("Language:", dev.language)
print("Experience:", dev.experience)

##5.bank account-> saving account-> premiusm account
class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print("New balance:", self.balance)


class SavingsAccount(BankAccount):
    def __init__(self, owner, balance, interest_rate):
        super().__init__(owner, balance)
        self.interest_rate = interest_rate

    def add_interest(self):
        interest = self.balance * self.interest_rate / 100
        self.balance += interest
        print("Interest added:", interest)


class PremiumSavingsAccount(SavingsAccount):
    def __init__(self, owner, balance, interest_rate, bonus):
        super().__init__(owner, balance, interest_rate)
        self.bonus = bonus

    def add_bonus(self):
        self.balance += self.bonus
        print("Bonus added:", self.bonus)


account = PremiumSavingsAccount("Aman", 10000, 5, 500)

account.deposit(1000)
account.add_interest()
account.add_bonus()

print("Final Balance:", account.balance)
