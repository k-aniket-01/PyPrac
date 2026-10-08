"""Exercise 7: Light Class with On/Off State Toggle
Problem Statement: Write a Python program to create a Light class with three methods: turn_on() that switches 
the light on, turn_off() that switches it off, and status() that reports whether the light is currently on off.

Purpose: This exercise models a simple stateful object, where the object remembers and changes its own 
condition over time. It introduces the concept of state management within a class, a pattern found everywhere 
from UI components and IoT devices to game objects and workflow engines.

Given Input: Create a Light object, call turn_on(), check status(), call turn_off(), and check status() again.

Expected Output:

Light is ON
Current status: ON
Light is OFF
Current status: OFF"""
class Light():
    def __init__(self, ):
        self.light = False
    
    def turn_on(self):
        self.light = True

    def turn_of(self):
        self.light = False
        
    def status(self):
        return "ON" if self.light else "OFF"
    
a = Light()
print(a.status())
a.turn_on()
print(a.status())
a.turn_of()
print(a.status())