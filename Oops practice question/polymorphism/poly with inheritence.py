class vehicle:
    def start(self):
        print("vehicle starts")
        
class car(vehicle):
    def start(self):
        print("car start with the key")
        
class bike(vehicle):
    def start(self):
        print("bike start with button")
        
vehicle1=[car(),bike()]

for vehicle in vehicle1:
    vehicle.start()