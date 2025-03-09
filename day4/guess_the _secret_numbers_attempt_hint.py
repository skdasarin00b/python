a=int(input("Enter a number: "))
attempt=0
hint=0
while a!=7:
    attempt +=1
    a = int(input("Enter a number: "))
    if attempt%1==0:
        print("Psst! the secret number is below 10")
    a = int(input("Enter a number: "))
print("Yup the number is 7")