# A program which takes Radius as input and prints Diameter, Area and Parimeter of that Circle.

r = float(input("Enter Radius of Circle = "))

d = 2*r
ar = 3.14*r**2
pa = 2*3.14*r

print("-----------------------------")
print("Diameter of Circle  = ",d)
print("Area of Cicle       = ",round(ar,3))
print("Parimeter of Circle = ",round(pa,3))
print("-----------------------------")
