# A program which takes any range as input and prints sum of following series upto that range,
# 1 + x^1/1! - x^2/2! + x^3/3! +........+ x^n/n!

b = int(input("Enter Base  = "))
r = int(input("Enter Range = "))
po = 1
Sum = 1
f = 1

for i in range (1, r+1):
    po *= b
    f  *= i
    div = po/f
    if (i % 2 == 0):
        Sum -= div
    else:
        Sum += div
    
print("----------------------------------------------------------")
print("Sum of 1+x^1/1!-x^2/2!+x^3/3!+... upto range {0} = {1}".format(r, round(Sum, 3)))
print("----------------------------------------------------------")