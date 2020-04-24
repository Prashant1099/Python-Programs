# A program which takes any number as input and prints Factorial of that number.

n = int(input("Enter any Number = "))
f = 1

for i in range (1, n+1):
    f *= i

print("----------------------------")
print("Factorial of {0} = {1}".format(n, f))
print("----------------------------")