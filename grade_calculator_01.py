student_grade = float(input("What is your grade? "))
# math
remain = student_grade % 10
if remain >= 0 and remain < 3:
    sign = "-"
elif remain >= 7:
    sign = "+"
else:
    sign = " "
print()
pass_course = False

if student_grade >= 90:
    if student_grade > 90 and student_grade < 93:
        print(f"Grade: A{sign}")
        pass_course = True
    else:
        print("Grade: A")
    pass_course = True

elif student_grade >= 80:
    print(f"Grade: B{sign}")
    pass_course = True

elif student_grade >= 70:
    print(f"Grade: C{sign}")
    pass_course = True

elif student_grade >= 60:
    print(f"Grade: D{sign}")
    pass_course = False

else:
    if student_grade < 60:
        print("Grade: F")
        pass_course = False

if pass_course:
    print("Congratulations! You did a great job.")
else:
    print("We are very sorry. Try harder the next time.")
