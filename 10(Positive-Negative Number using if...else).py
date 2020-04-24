# A program which takes any Number as input and checks whether that Number is Positive or Negative.

n = int(input("Enter any Number = "))

print("--------------------------")
if (n > 0):
    print(n,"is Positive Number")
elif (n < 0):
    print(n, "is Negative Number")
else:
    print("Enterd Number is Zero")
print("--------------------------")