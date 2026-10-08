"""Exercise 3: Rectangle Class with Area & Perimeter
Problem Statement: Write a Python program to create a Rectangle class with length and width as instance 
attributes, and two methods: area() that returns the area and perimeter() that returns the perimeter.

Purpose: Learn how to add instance methods to a class. Methods allow objects to perform operations using 
their own data, which is a key principle of encapsulation in OOP. Calculating geometric properties is a clean, 
practical context for understanding how self connects methods to instance data.

Given Input: rect = Rectangle(10, 4)

Expected Output: Area = 40 and Perimeter = 28"""

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return f'Area = {self.length * self.width}'
    def perimeter(self):
        return f'Perimeter = {2 *(self.length + self.width)}'
    
a = Rectangle(10,4)
print(a.area())
print(a.perimeter())