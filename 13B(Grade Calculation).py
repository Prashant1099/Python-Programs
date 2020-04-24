# A program which takes Percentage as input and prints Grade accordingly.

per = float(input("Enter Percentage = "))

if (per <= 40):
    grade = "E"
elif (per <= 50):
    grade = "D"
elif (per <= 60):
    grade = "C"
elif (per <= 80):
    grade = "B"
else:
    grade = "A"

print("--------------")
print("Grade = ",grade)
print("--------------")