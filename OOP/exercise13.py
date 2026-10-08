"""Exercise 13: Bus Subclass Inheriting from Vehicle
Problem Statement: Write a Python program to create a Vehicle parent class with name and max_speed attributes 
and a display() method. Then create a Bus child class that inherits everything from Vehicle without adding 
anything new, and confirm that an instance of Bus can access the parents method.

Purpose: This exercise introduces inheritance, one of the four pillars of OOP. Inheritance lets a child class 
automatically receive all attributes and methods from its parent, promoting code reuse and expressing natural 
“is-a” relationships. A Bus is a Vehicle, so it makes sense for it to share the same interface.

Given Input: bus1 = Bus("School Bus", 120)

Expected Output: Vehicle: School Bus, Max Speed: 120 km/h

"""
class Vehicle():
    def __init__(self, name, max_speed):
        self.name = name
        self.max_speed = max_speed

    def display(self):
        return self.name , self.max_speed

class Bus(Vehicle):
    pass

bus1 = Bus("School Bus", 120)
print(bus1.display())