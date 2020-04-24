# A program which takes any Amount as input and prints Tax and Net Amount.

amt = float(input("Enter Amount = "))

if (amt <= 10000):
    tax = 0
elif(amt <= 20000):
    tax = (amt * 10)/100
elif (amt <= 30000):
    tax = (amt * 20)/100
else:
    tax = (amt * 30)/100

net = amt + tax

print("---------------------------")
print("Tax        = ", tax)
print("Net Amount = ", net)
print("---------------------------")
