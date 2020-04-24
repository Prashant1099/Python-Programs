# A program which takes any range as input and prints sum of following series upto that range,
# 1 + 1! + 2! + 3! +.......+ n!

r = int(input("Enter any Range = "))
Sum = 1
f = 1

for i in range(1, r+1):
    f *= i
    Sum += f

print("-----------------------------------------------")
print("Sum of 1+1!+2!+3!+... upto range {0} = {1}".format(r, Sum))
print("-----------------------------------------------") 