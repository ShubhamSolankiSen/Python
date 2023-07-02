# Write a program to calculate the grade of a student from his marks from the following scheme:

marks = int(input("Enter your marks:\n"))

if marks>90:
    print("Ex")

elif marks>=80:
    print("A")

elif marks>=70:
    print("B")

elif marks>=60:
    print("C")

elif marks>=50:
    print("D")

else:
    print("F")