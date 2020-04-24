# A program which takes any Range as input and Prints Fibonacci Series Upto that range.

r = int(input("Enter any Range = "))
b, e = 0, 1

print("------------------------------------------------------------------")
print("Fibonacci Series upto Range {0} : {1},{2}".format(r, b, e), end = ',')

for i in range (3, r+1):
    Sum = b + e
    if (i == r):
        print(Sum, end = ' ')
    else:
        print(Sum, end = ',')
    b = e
    e = Sum
print()
print("------------------------------------------------------------------")