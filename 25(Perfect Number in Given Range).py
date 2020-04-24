# A program which takes any Range as input and Prints Perfect Numbers in that range.

r = int(input("Enter Range = "))

print("--------------------------------------")
print("Perfect Numbers upto range {0} are :- ".format(r))
print("--------------------------------------")

for i in range (1, r+1):
    tot = 0
    temp = i
    for j in range (1, i):
        if (i % j == 0):
            tot += j
    
    if (temp == tot):
        print(temp)
print("--------------------------------------")        