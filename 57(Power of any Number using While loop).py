# A program which takes Base and Expo as input and prints Power accordingly.

b = int(input("Enter Base = "))
e = int(input("Enter Expo = "))

i = po = 1
while (i <= e):
    po *= b
    i += 1

print("------------------------------")
print("{0} to the Power {1} = {2}".format(b, e, po))
print("------------------------------")