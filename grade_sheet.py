#create a college gradesheet using python 


grade_sheet = float(input("Enter your grade :"))

if grade_sheet >=90 and grade_sheet <= 100:
    print("Your grade is A")
elif grade_sheet >=80 and grade_sheet <= 89:
    print("Your grade is B")
elif grade_sheet >=70 and grade_sheet <= 79:
    print("Your grade is C")
elif grade_sheet >=60 and grade_sheet <= 69:
    print("Your grade is D")
elif grade_sheet >=50 and grade_sheet <= 59:
    print("Your grade is E")
else:
    print("Your grade is F")
    