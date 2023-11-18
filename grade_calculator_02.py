student_grade = float(input("What is your grade? "))
print()
pass_course = False
if student_grade >= 90:
    if student_grade >= 93:
        print("Grade: A")
        pass_course = True
    else:
        print("Grade: A-")
        pass_course = True

elif student_grade >= 80:
    if student_grade >= 87:
        print("Grade: B+")
        pass_course = True
    elif student_grade < 83 and student_grade >= 80:
        print("Grade: B-")
        pass_course = True
    else:
        print("Grade: B")
        pass_course = True

elif student_grade >= 70:
    if student_grade >= 77:
        print("Grade: C+")
        pass_course = True
    elif student_grade < 73 and student_grade >= 70:
        print("Grade: C-")
        pass_course = True
    else:
        print("Grade: C")
        pass_course = True

elif student_grade >= 60:
    if student_grade >= 67:
        print("Grade: D+")
        pass_course = False
    elif student_grade < 63 and student_grade >= 60:
        print("Grade: D-")
        pass_course = False
    else:
        print("Grade: D")
    pass_course = False
else:
    if student_grade < 60:
        print("Grade: F")
        pass_course = False

if pass_course:
    print("Congratulations! You did a great job.")
else:
    print("We are very sorry. Try harder the next time.")
