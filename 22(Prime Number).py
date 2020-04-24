# A program which takes any Number as input and checks whether the Number is Prime or not.

n = int(input("Enter any Number = "))
count = 0

for i in range (2, n):
    if (n % i == 0):
        count += 1

print("---------------------------")
if (count == 0):
    print(n,"is a Prime Number")
else:
    print(n,"is not a Prime Number")
print("---------------------------")
