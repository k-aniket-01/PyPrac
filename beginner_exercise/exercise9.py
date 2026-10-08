"""
Exercise 9. Vowel Frequency Counter
Practice Problem: Write a program to count the total number of vowels (a, e, i, o, u) present in a 
given sentence.

Exercise Purpose: This exercise introduces “Membership Testing.” By checking if a character belongs 
to a specific group (the vowels), you learn how to filter data based on categories. This is a 
fundamental step toward building text-analysis tools or spam filters.

Given Input: sentence = "Learning Python is fun!"

Expected Output: Number of vowels: 6"""

sentence = "Learning Python is fun!"
c = 0
vowels = 'AEIOUaeiou'

for i in sentence:
    if i in vowels:
        c +=1
        
print(c)