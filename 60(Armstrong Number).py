# A program which takes any Number as input and checks whether the Number is Armstrong Number or 
# not.

n = int(input("Enter any Number = "))
temp = n
Sum = 0

while (n > 0):
    mod = n%10
    print("mod = ",mod)
    Sum += mod**3
    print("sum = ",Sum)
    n = n//10

print(Sum)
print("---------------------------------")
if (temp == Sum):
    print(temp,"is Armstrong Number")
else:
    print(temp,"is not a Armstrong Number")
print("---------------------------------")