# A program which takes Range is input and prints Prime Number in that range.

r = int(input("Enter Range = "))

print("---------------------------------")
print("Prime Numbers Upto range {0} are :-".format(r))
print("---------------------------------")
for i in range(1, r+1):
    count = 0
    for j in range (2, i):
        if (i % j == 0):
            count += 1

    if (count == 0):
        print(i)
print("---------------------------------")