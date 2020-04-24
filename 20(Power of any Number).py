# A program which takes Base and Exponent as input and prints Power accordingly.

b = int(input("Enter Base = "))
e = int(input("Enter Expo = "))
po = 1

print("---------------------------------")
for i in range (1, e+1):
    po = po * b

print("{0} to the Power {1} = {2}".format(b, e, po))
print("---------------------------------")