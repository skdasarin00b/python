a=int(input("Enter a number, It should be a palindrome: "))
original_num=a
rev=0
while a!=0:
    n=a%10
    rev=rev*10+n
    a//=10
print(rev)
if original_num==rev:
    print(f"The number {original_num} is a palindrome")
else:
    print(f"The number {original_num} is not a palindrome as the value is {rev}")

