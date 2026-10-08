"""Exercise 4: Student Class with Average Grade
Problem Statement: Write a Python program to create a Student class that stores a students name and a list 
of marks. Add a method average() that calculates and returns the average of all marks.

Purpose: This exercise shows how instance attributes can store complex data types such as lists, not just 
simple values. It also practices combining OOP with list operations and arithmetic, a pattern common in 
gradebooks, dashboards, and reporting tools.

Given Input: s1 = Student("Alice", [85, 90, 78, 92, 88])

Expected Output: Alice's Average Grade: 86.6"""

class Student():
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
    
    def average_grade(self):
        return total(self.marks) / len(self.marks)
    
a = Student("Alice", [85, 90, 78, 92, 88])
print(f"{a.name}'s average marks = {a.average_grade()} ")