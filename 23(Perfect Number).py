# A program which takes any Number as input and checks whether the Number is Perfect Number or 
# not.

n = int(input("Enter any Number = "))
tot = 0
temp = n

for i in range (1, n):
    if (n % i == 0):
        tot += i

print("----------------------------")
if (temp == tot):
    print(n,"is a Perfect Number")
else:
    print(n,"is not a Perfect Number")
print("----------------------------")

