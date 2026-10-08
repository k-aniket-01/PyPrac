"""Exercise 14: verride Parent Method Using super()
Problem Statement: Write a Python program where a Vehicle parent class has a seating_capacity() method that 
accepts a capacity argument. Create a Bus child class that overrides this method to provide a default seating 
capacity of 50, using super() to call the parents version internally.

Purpose: This exercise covers method overriding and the use of super(), two key tools in OOP inheritance. 
Overriding lets a child class customize or extend a parent methods behavior without rewriting it from scratch. 
super() delegates part of the work back to the parent, keeping the code DRY and maintaining the original logic 
as a foundation.

Given Input: bus = Bus("School Bus", 120)

Expected Output: School Bus seating capacity is: 50"""

class Vehicle():
    def __init__(self, name, max_spped):
        self.name = name
        self.max_speed = max_spped

    def capacity(self, capacity):
        print(f"name is {self.name}, max speed is {self.max_speed} and capacity is {capacity}")
class Bus(Vehicle):
    def capacity(self):
        super().capacity(50)
bus1 = Bus("volvo", 120)
bus1.capacity()