# A program which takes any number as input and prints Factorial of that Number using while loop.

n = int(input("Enter any Number = "))

i = f = 1
while (i <= n):
    f *= i
    i += 1

print("-------------------------------")
print("Factorial of {0} = {1}".format(n, f))
print("-------------------------------")