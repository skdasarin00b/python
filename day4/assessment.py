grade=float(input("Enter the grade of student"))
if grade>=90:
    print("The grade of the student is A")
else:
    if grade >= 80:
        print(f"The grade of the student is {grade} and the rank is B")
    else:
        if grade>=70:
            print(f"The grade of the student is {grade} and the rank is C")
        else:
            if grade>=60:
                print(f"The grade of the student is {grade} and the rank is D")
            else:
                print("The student has Failed")