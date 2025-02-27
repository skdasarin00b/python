
# Task:
# Write a Python program that takes two numbers as input from the user and:

#     Adds, subtracts, multiplies, and divides them.
#     Determines which number is larger.
#     Checks if the sum of the numbers is even or odd.

# Requirements:

#     Use input() to get user inputs.
#     Convert inputs to integers.
#     Use conditionals (if, else) to determine the larger number.
#     Use the modulo operator % to check if the sum is even or odd.

# Enter first number: 10
# Enter second number: 5
# Addition: 15
# Subtraction: 5
# Multiplication: 50
# Division: 2.0
# Larger number: 10
# The sum is odd.


a=int(input("Enter first num: "))
b=int(input("Enter second num: "))
c=a+b
d=a-b
e=a*b
f=a/b
print(f"Addition: {c}")
print(f"Subtraction: {d}")
print(f"Multiplication: {e}")
print(f"Division: {round(f,2)}")
g=[c, d , e, f]
print(g)
g.sort(reverse=True)
m=max(g)
print(m)
if c%2==0:
    print("The result is even")
else:
    print("The result is odd")