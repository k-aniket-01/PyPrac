"""Exercise 6: Bank Account with Deposit & Overdraw Protection
Problem Statement: Write a Python program to create a BankAccount class with a balance attribute and 
two methods: deposit(amount) that adds funds to the balance, and withdraw(amount) that deducts funds 
but prevents the balance from going below zero.

Purpose: Learn data validation and conditional logic inside instance methods. Preventing overdraw is a 
real-world business rule, and implementing it here teaches you how classes can enforce constraints on 
their own data, a core idea behind encapsulation in OOP.

Given Input: Starting balance of 1000, deposit 500, withdraw 200, then attempt to withdraw 2000.

Expected Output:

Balance after deposit: 1500
Balance after withdrawal: 1300
Insufficient funds. Current balance: 1300"""
class Bank():
    def __init__(self, balance):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        # return f"Balance after deposit: {self.balance}"
    
    def withdraw(self, amount):
        if self.balance <= amount:
            return f"Insufficient funds. Current balance: {self.balance}"
        self.balance -= amount
        # return f"Balnce after withdrawal: {self.balance}"

a = Bank(1000)
print(f"balance : {a.balance}")
a.deposit(200)
print(f"balance after deposite: {a.balance}")
a.withdraw(500)
print(f"Balance after withdrawal: {a.balance}")
b= a.withdraw(2000)
print(b)