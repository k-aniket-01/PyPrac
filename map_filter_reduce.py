
#map
numbers = [2, 4, 6, 8, 10]
print(list(map(lambda  x :x*x, numbers)))

numbers = [1, 2, 3, 4, 5]
print(list(map(lambda x : x**3, numbers)))

numbers = [10, 20, 30, 40]
print(list(map(lambda x : str(x), numbers)))

nums = ["100", "200", "300", "400"]
print(list(map(lambda x: int(x), nums)))

names = ["aniket", "rahul", "amit", "priya"]
print(list(map(lambda x: x.upper(), names)))

names = ["ANIKET", "RAHUL", "AMIT"]
print(list(map(lambda x: x.lower(), names)))

words = ["python", "java", "go", "javascript"]
print(list(map(lambda x: len(x), words)))

names = ["  Aniket ", " Rahul ", " Amit  "]
print(list(map(lambda x: x.strip(), names)))

names = ["aniket", "rahul", "amit"]
print(list(map(lambda x:x.capitalize(), names)))

words = ["python", "hello", "world"]
print(list(map(lambda x:x[::-1], words)))

a = [1, 2, 3]
b = [4, 5, 6]
print(list(map(lambda x,y: x+y, a,b)))

a = [2, 3, 4]
b = [5, 6, 7]
print(list(map(lambda x,y: x*y, a,b)))

first = ["Aniket", "Rahul", "Amit"]
last = ["Khomane", "Sharma", "Patil"]
print(list(map(lambda f,l : f"{f} {l}", first,last)))

a = [10, 30, 50]
b = [20, 25, 60]
print(list(map(lambda a,b:a if a > b else b , a,b)))

def squeare(x):
    return x*x
print(list(map(squeare, [1,2,3,4,5])))


#filter
import random
def sample(n=10):
    l=[]
    for i in range(n):
        l.append(random.randint(-100,200))
    return l
a=sample()
print(a)
print(list(filter(lambda x:x%2==0,a)))
print(list(filter(lambda x:x%2!=0,a)))
print(list(filter(lambda x:x>100, a)))
print(list(filter(lambda x: x<50, a)))
print(list(filter(lambda x:x>0, a)))


#reduce()
from functools import reduce

import random
def sample(n=10):
    return [random.randint(1,10) for _ in range(n)]
s=sample()
print(s)
print(reduce(lambda a,b:a+b, s))
print(reduce(lambda a,b:a*b, s))
print(reduce(lambda a,b:a if a>b else b , s))
print(reduce(lambda a,b:a if a<b else b , s))
t = ["Aniket", "Rahul", "Amit"]
print(reduce(lambda a,b:a+b, t))

employees = [
    ("Aniket", 25000),
    ("Rahul", 32000),
    ("Amit", 28000)
]
