"""Given Input:

remove_chars("pynative", 4)
remove_chars("pynative", 2)

Expected Output:

tive
native"""

def remove_chars(s,n):
    return s[n:]

print(remove_chars("pynative", 4))
print(remove_chars("pynative", 2))