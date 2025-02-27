# Python Task (Basic Difficulty - Day 3)

# Task: Write a Python program that checks if a given string is a palindrome (a word, phrase, or sequence that reads the same backward as forward). Ignore case and non-alphanumeric characters.
# Input: "A man, a plan, a canal: Panama"
# Output: True

# Input: "race a car"
# Output: False

#
# a=str(input("Enter text: "))
# s=a[::-1]
# print(s)
# if a==s:
#     print(f"{a} is a palindrome")
# else:
#     print(f"{a} is not a palindrome")

# import re
# def palindrome(s):
#     s=re.sub(r'[^a-zA-Z0-9]','',s.lower())
#     return s==s[::-1]
# a=input("Enter text: ")
# if palindrome(a)==True:
#     print(f"{a} is a palindrome")
# else:
#     print(f"{a} is not palindrome")

# import re
# def palindrome(s):
#     re.sub("a-zA-Z0-9",'',s.lower())
#     print(s[::-1])
#     return s==s[::-1]
# a=input("Enter a text: ")
# if palindrome(a):
#     print(f"{a} is a palindrome")
# else:
#     print(f"{a} is not palindrome")
    
# Task: Write a Python program that takes a number as input and checks if it is a prime number.
# Requirements:

#     The function should return True if the number is prime, otherwise False.
#     Handle edge cases (e.g., numbers less than 2).
#     Optimize the solution using a loop that runs only up to the square root of the number.

# a=int(input("Enter a number: "))
# if a>1:
#     for i in range(2, (a//2)+1):
#         if a%i==0:
#             print(a,"is not prime")
#             break
#     else:
#         print(f"{a} is a prime number")
# else:
#     print(f"{a} is not a prime")
import math
a=int(input("Enter a number: "))
if a<2:
    for i in range(2, int(math.sqrt(a))+1):
        if a%i==0:
            print(a)
            print(f"{a} is not prime number")
            break
    else:
        print(a)
        print(f"{a} is prime")
else:
    print(a)
    print(f"{a} is not prime")
            














