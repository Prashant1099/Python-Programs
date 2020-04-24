# A program which takes any three number as input and prints Greatest number among them.

a = int(input("Enter First Number  = "))
b = int(input("Enter Second Number = "))
c = int(input("Enter Third Number  = "))

print("--------------------------------")
if (a == b and a == c):
    print("All Numbers are Equal")
elif (a > b and a > c):
    print("{0} is Greater than {1} and {2}".format(a, b, c))
elif (b > c):
    print("{0} is Greater than {1} and {2}".format(b, a, c))
else:
    print("{0} is Greater than {1} and {2}".format(c, a, b))
print("--------------------------------")