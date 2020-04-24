# With Argument

def power(b, e):
    po = 1

    for i in range (e):
           po = po * b
    
    print(b, "to the Power", e, "=",po)

b = int(input("Enter Base = "))
e = int(input("Enter Expo = "))
power(b, e)
    
