#1. Write a Python program to create a Train class with max_speed and Coaches instance attributes.
#	a. Create a Taxi object that will inherit all of the variables and methods of the parent Train class and display it.
#	b. Create a Car class that inherits from the Train class. Give the capacity argument of Metro.seating_capacity() a default value of 5
#	c. Define a property that must have the same value for every class instance (object).
#	d. Create a Metro child class that inherits from the Train class. The default fare charge of any Train is seating capacity * 100. 
#  If Train is Metro instance, we need to add an extra 10% on full fare as a maintenance charge. So total fare for bus instance will become
#     the final amount = total fare + 10% of the total fare.
class Train:
    color = "Red"
    def __init__(self, max_speed, Coaches, capacity):
        self.max_speed = max_speed
        self.Coaches = Coaches
        self.capacity = capacity
    def fare(self):
        f = self.capacity * 100
        return f
    def display(self):
        return f"{self.__class__.__name__} Max Speed : {self.max_speed} Coaches : {self.Coaches}, Capacity : {self.capacity}"
passengerTrain = Train(40, 15, 50)
print(passengerTrain.display())
print(f"Total Fare : {passengerTrain.fare()}")
class GoodsTrain(Train):
    pass
class Metro(Train):
    def __init__(self, max_speed, Coaches, capacity=5):
        super().__init__(max_speed, Coaches, capacity)
    def fare(self):
        cost = super().fare()
        cost += cost * 0.1
        return cost
Hyd_Metro = Metro(80, 20, 70)
print(Hyd_Metro.display())
print(f"Total Fare : {Hyd_Metro.fare()}")
print("\n\n")
