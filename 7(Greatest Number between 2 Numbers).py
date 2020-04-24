# A program which takes any two number as input and prints Greatest number among them.

a = int(input("Enter First Number  = "))
b = int(input("Enter Second Number = "))

print("--------------------------------")
if (a > b):
    print("{0} is Greater than {1}".format(a, b))
elif (a < b):
    print("{0} is Greater than {1}".format(b, a))
else:
    print("Both Numbers are Equal")
print("--------------------------------")