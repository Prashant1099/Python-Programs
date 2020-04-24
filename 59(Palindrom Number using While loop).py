# A program which takes any Number as input checks whether the number is Palindrom or not.

n = int(input("Enter any Number = "))
temp = n
rev = 0

while (n > 0):
    mod = n%10
    rev = rev*10 + mod
    n = n//10

print("-------------------------------------")
if (temp == rev):
    print(temp,"is a Palindrom Number")
else:
    print(temp,"is not a Palindrom Number")
print("-------------------------------------")