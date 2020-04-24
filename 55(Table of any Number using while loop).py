# A program which takes any Number as input and prints Table of that Number.

n = int(input("Enter any Number = "))

i = 1
print("--------------------")
while (i < 11):
    print("{0} x {1:2} = {2:3}".format(n, i, n*i))
    print("--------------------")
    i += 1