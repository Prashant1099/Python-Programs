# A program which prints Roots of Quadratic Equation.
import math

a = int(input("Enter A = "))
b = int(input("Enter B = "))
c = int(input("Enter C = "))

d = (b**2)-(4*a*c)
print("----------------------------------------")
print("D = ",d)

if (d > 0):
    print("\nThe Equation contains two Different roots :")

    r1 = (-b + math.sqrt(d))/(2*a)
    r2 = (-b - math.sqrt(d))/(2*a)

    print("First Root  = ", round(r1,3))
    print("Second Root = ", round(r2,3))
elif (d == 0):
    print("\nThe Equation contains same roots :")

    r1 = r2 = (-b/(2*a))

    print("First Root  = ", round(r1,3))
    print("Second Root = ", round(r2,3))
else:
    print("\nThe Equation contains Imaginary roots :")
print("----------------------------------------")
