"""Exercise 10. Finding Extremes (Min/Max) in a List

Practice Problem: Given a list of integers,find and print both  largest and  smallest numbers.

Exercise Purpose: This exercise explores “Aggregate Functions.” While Python has built-in tools 
this, understanding how to identify extremes is critical for data normalization, where you often 
need to find the range of a dataset before processing it.

Given Input: nums = [45, 2, 89, 12, 7]

Expected Output: Largest: 89 Smallest: 2"""

nums = [45, 2, 89, 12, 7]
lar = nums[0]
sml = nums[0]

for i in nums:
    if i > lar:
        lar = i
    if i < sml:
        sml = i

print(lar,sml)



