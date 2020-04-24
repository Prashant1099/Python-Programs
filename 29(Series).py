# A program which takes any range as input and prints sum of following series upto that range,
# 1/1+1/2+1/3+.......+1/n

r = int(input("Enter any Range = "))
Sum = 0

for i in range(1, r+1):
    Sum += 1/i
    
print("-----------------------------------------------")
print("Sum of 1/1+1/2+1/3+.... upto range {0} = {1}".format(r, round(Sum, 3)))
print("-----------------------------------------------")
