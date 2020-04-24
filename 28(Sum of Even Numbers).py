# A program which takes any Range as input and prints Sum of Even Numbers upto that range.

r = int(input("Enter any Range = "))
Sum = 0

for i in range (2, r+1, 2):
    Sum += i

print("-----------------------------------------------")
print("Sum of Even Numbers upto range {0} = {1}".format(r, Sum))
print("-----------------------------------------------")
