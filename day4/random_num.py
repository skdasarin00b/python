import random
secret_number=random.randint(1,100)
a=int(input("Guess a number between 1 to 100: "))
attempt=0
hint=secret_number%10
hint2=secret_number//10
while a!=secret_number:
    attempt+=1
    if a<secret_number:
            print(f"The guessed number is lower. Try something bigger")
    elif a>secret_number:
            print(f"The guessed number is higher. Try something lower")
    if attempt%2==0:
       hint=secret_number%10
       print(f"The last digit of guessed number is {hint}")
    if attempt%8==0:
        hint2=secret_number//10
        print(f"The first digit of the number is {hint2}")
    a = int(input("Try again: "))
print(f"Congratulations! Human {a} is the correct number")
if attempt>8:
    print(f"you guessed it in {attempt} attempts! Wow so clever")
elif attempt<5:
    print(f"you guessed it in {attempt} attempts! good")

