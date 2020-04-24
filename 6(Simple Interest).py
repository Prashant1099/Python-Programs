# A program which takes Principal amount, rate and time as input and prints Simple Interest and 
# Net amount.

p = float(input("Enter Principal Amount = "))
r = float(input("Enter Rate             = "))
t = float(input("Enter Time             = "))

si = (p * r * t)/100
net = si + p

print("------------------------------------------")
print("Simple Interest = ", round(si, 3)
print("Net Amount      = ", round(net, 3)
print("------------------------------------------")