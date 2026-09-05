# dynamic variable
firstname = input("What is your first name? ")
surname = input("What is your surname? ")
age = input("What is your age? ")
gpa = input("What is your GPA score? ")
student = input("Are you a student? ")

# date type
firstname = (str(firstname))
surname = (str(surname))
age = (int(age))
gpa = (float(gpa))
# student =(bool(student))
student = student.lower() == "yes"



print(firstname)
print(surname)
print(age)
print(gpa)
print(student)