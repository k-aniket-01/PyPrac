"""Practice Problem: Write a program that takes a string and reverses it 
(e.g., “Python” becomes “nohtyP”).

Exercise Purpose: This exercise demonstrates “Sequence Slicing.” Strings in Python are sequences,
and mastering the slicing syntax is a powerful shortcut for data manipulation that would take 5-10 
lines of code in other languages.

Given Input: text = "Python"

Expected Output: Reversed: nohtyP"""

s= 'Python'
print(s[::-1])

rev = ''
for i in s:
    rev = i + rev
print(rev)
    
