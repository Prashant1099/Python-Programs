# A program which takes any Number as input and prints table of that number.

n = int(input("Enter any Number = "))

print("----------------")
for i in range (1, 11):
    print("{0} x {1:2} = {2:3}".format(n, i, n*i))
    print("----------------")