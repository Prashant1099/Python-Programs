# A program which takes any three Numbers as input and Swap them, without using third variable.

a = int(input("Enter First Number  = "))
b = int(input("Enter Second Number = "))
c = int(input("Enter Third Number  = "))

c = a + b + c
a = c - (a + b)
b = c - (a + b)
c = c - (a + b)

print("-----------------------")
print("After Swapping")
print("-----------------------")
print("First Number  = ",a)
print("Second Number = ",b)
print("Third Number  = ",c)
print("-----------------------")