"""Exercise 8: User Class with Password Validation
Problem Statement: Write a Python program to create a User class that stores a username and a password. 
Add a check_password(input_password) method that returns True if the input matches the stored password, 
and False otherwise.

Purpose: This exercise introduces the idea of controlled access to sensitive data inside a class. Rather
 than exposing the password directly, the class provides a dedicated method to verify it. This pattern 
 reflects a core principle of encapsulation in OOP, where internal data is protected and accessed only 
 through defined interfaces.

Given Input: u1 = User("alice", "secure123")

Expected Output:

True
False"""
class Validation():
    def __init__(self, user, password):
        self.user = user
        self.password = password

    def checker(self, password):
        if self.password == password:
            print(True)
        else:
            print(False)

a = Validation("Aniket", "pass")

a.checker("test")