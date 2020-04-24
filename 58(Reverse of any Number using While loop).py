# A program which takes any Numer as input and prints Reverse and Summation of that Digit.

n = int(input("Enter any Number = "))

temp = n
rev = Sum = 0

while (n > 0):
    mod = n%10
    rev = rev*10 + mod
    Sum += mod
    n = n//10

print("---------------------------------")
print("Reverse of {0}   = {1}".format(temp, rev))
print("Summation of {0} = {1}".format(temp, Sum))
print("---------------------------------")