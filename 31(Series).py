# A program which takes any range as input and prints sum of following series upto that range,
# 1 + x^1 + x^2 + x^3 +......+ x^n

b = int(input("Enter Base  = "))
r = int(input("Enter Range = "))
Sum = 1
po = 1

for i in range (1, r+1):
    po *= b   
    Sum += po

print("-----------------------------------------------")
print("Sum of 1+x^1+x^2+x^3+... upto range {0} = {1}".format(r, Sum))
print("-----------------------------------------------") 