# A program which takes any three Numbers as input and Swap them, using third variable.

a = int(input("Enter First Number  = "))
b = int(input("Enter Second Number = "))
c = int(input("Enter Third Number  = "))

temp = c
c = b
b = a
a = temp

print("-----------------------")
print("After Swapping")
print("-----------------------")
print("First Number  = ",a)
print("Second Number = ",b)
print("Third Number  = ",c)
print("-----------------------")