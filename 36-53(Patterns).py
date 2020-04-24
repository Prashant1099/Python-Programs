# A program which takes Range as input and prints Different patterns upto that Range.

r = int(input("Enter Range = "))

print("-----------------------------")              #36
for row in range (1, r+1):
    for col in range (1, row+1):
        print(col, end = " ")
    print()
print("-----------------------------")

for row in range (1, r+1):                          #37
    for col in range (1, row+1):
        print(row, end = " ")
    print()
print("-----------------------------")

for row in range (1, r+1):                          #38
    for col in range (1, row+1):
        print(row%2, end = " ")
    print()
print("-----------------------------")

for row in range (1, r+1):                          #39
    for col in range (1, row+1):
        print(col%2, end = " ")
    print()
print("-----------------------------")

for row in range (1, r+1):                          #40
    for col in range (1, row+1):
        print(row*col, end = " ")
    print()
print("-----------------------------")

x = 1
for row in range (1, r+1):                          #41
    for col in range (1, row+1):
        print(x, end = " ")
        x += 1
    print()
print("-----------------------------")

x = 65
for row in range (1, r+1):                          #42
    for col in range (1, row+1):
        print(chr(x), end = " ")
        x += 1
    print()
print("-----------------------------")

x = 65
for row in range (1, r+1):                          #43
    for col in range (1, row+1):
        print(chr(x), end = " ")
        x += 1
    x = 65
    print()
print("-----------------------------")

x = 65                                              #44
for row in range (1, r+1):
    for col in range (1, row+1):
        print(chr(x), end = " ")
    x += 1
    print()
print("-----------------------------")

for row in range (1, r+1):                          #45
    for sp in range (1, r-row+1):
        print("  ", end = "")
    for col in range (1, row+1):
        print("*", end = " ")
    print()
print("-----------------------------")

for row in range (1, r+1):                          #46
    for col in range (1, r-row+2):
        print("*", end = " ")
    print()
print("-----------------------------")

for row in range (1, r+1):                          #47
    for sp in range (1, row):
        print("  ", end = "")
    for col in range (1, r-row+2):
        print("*", end = " ")
    print()
print("-----------------------------")

for row in range (1, r+1):                          #48
    for sp in range (1, r-row+1):
        print("  ", end = "")
    for col in range (1, row+1):
        print("*", end = "   ")
    print()
print("-----------------------------")

for row in range (1, r+1):                          #49
    for sp in range (1, row):
        print("  ", end = "")
    for col in range (1, r-row+2):
        print("*", end = "   ")
    print()
print("-----------------------------")

for row in range (1, r+1):                          #50
    for sp in range (1, r-row+1):
        print("  ", end = "")
    for col in range (1, row+1):
        print("*", end = "   ")
    print()
for row in range (2, r+1):
    for sp in range (1, row):
        print("  ", end = "")
    for col in range (1, r-row+2):
        print("*", end = "   ")
    print()
print("-----------------------------")

for row in range (1, r+1):                          #51
    for sp in range(1, row):
        print("  ", end = "")
    for col in range (1, r-row+2):
        print("*", end = "   ")
    print()
for row in range (2, r+1):
    for sp in range (1, r-row+1):
        print("  ", end = "")
    for col in range (1, row+1):
        print("*", end = "   ")
    print()
print("-----------------------------")

for row in range (1, r+1):                          #52
    for col in range (1, r+1):
        if (row == 1 or row == r or col == 1 or col == r):
            print("*", end = " ")
        else:
            print("  ", end = "")
    print()
print("-----------------------------")

for row in range (1, r+1):
    for sp in range (1, row):
        print("  ", end = "")
    for col in range (1, r-row+2):
        if (row == col):
            print("*", end = " ")
        else:
            print(" ")
    print()
