# A program which takes any Year as input and prints whether that is Leap year or not.

y = int(input("Enter any Year = "))

print("------------------------")
if (y % 400 == 0):
    if (y % 100 == 0):
        print(y,"is Leap Year")
    else:
        print(y,"is not a Leap Year")
elif (y % 4 == 0):
    print(y,"is Leap Year")
else:
    print(y,"is not a Leap Year")
print("------------------------")    