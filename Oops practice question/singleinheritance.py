#1. basic  single inheiteance

class animal:
    #constructor call
    def eat(self):
        print(f"anilmal is eating")
        
    def bark(self):
        print(f"animal is barking")
        
        
class dog(animal):
    def walk(self):
        print(f"dog is walking")
        
        
dog1=dog()
dog1.eat()
dog1.bark()
dog1.walk()



#2. question of basic single inheritance 
class vehicle:
    def start(self):
        print("vehicle is start")
        
    def stop(self):
        print("vehicle is stop")
        
class car(vehicle):
    def drive(self):
        print("car is now drived")
        
        
toyta=car()
toyta.start()
toyta.stop()
toyta.drive()



#3.Q  single inhitence with constructor
class Car:

    # constructor
    def __init__(self, windows, doors, enginetype):
        self.windows = windows
        self.doors = doors
        self.enginetype = enginetype

    # instance method
    def drive(self):
        print(f"The person will drive the car {self.enginetype}")


# Parent object
car1 = Car(4, 5, "petrol")

print(car1)
car1.drive()


# Child class
class Tesla(Car):

    # child constructor
    def __init__(self, windows, doors, enginetype, is_self_driving):
        super().__init__(windows, doors, enginetype)
        self.is_self_driving = is_self_driving

    # child instance method
    def check_self_driving(self):
        print(f"Tesla supports self driving: {self.is_self_driving}")


# Child object
tesla1 = Tesla(4, 5, "electric", True)

tesla1.check_self_driving()
tesla1.drive()


        

     