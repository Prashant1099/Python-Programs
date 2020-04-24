# A program which takes any String as input prints them repetidly.

mystr = input("Enter String = ")
r = int(input("Enter Range  = "))

print("--------------------------------------")
for i in range (1, r+1):
    print("{0} -> {1}".format(i, mystr))
print("--------------------------------------")