# Write a Python program that asks the user to enter a number. The program should keep adding the digits of the number until the sum is a single-digit number.
# Finally, print the single-digit result.

a=int(input("Enter a number: "))
while a>=10:
    son=0
    while a>0:
        son+=a%10
        a//=10
    print(son)
    a=son
print(a)
# num = int(input("Enter a number: "))
#
# while num >= 10:  # Keep summing digits until it's a single digit
#     sum_digits = 0
#     while num > 0:
#         sum_digits += num % 10  # Extract last digit and add to sum
#         num //= 10  # Remove last digit
#
#     print(f"Sum of digits: {sum_digits}")  # Print the intermediate sum
#     num = sum_digits  # Update num with the sum
#
# print(f"Final single-digit sum: {num}")


