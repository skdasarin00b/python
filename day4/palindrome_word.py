a=input("Enter a word which is a palindrome: ")
original_value=a
rev=a[::-1]
if original_value==rev:
    print("The word is a palindrome")
else:
    print("Its not a palindrome")
    #added