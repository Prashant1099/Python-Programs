# Without Argument

def power():
    b = int(input("Enter Base = "))
    e = int(input("Enter Expo = "))
    po = 1

    for i in range (e):
           po = po * b
    
    print(b, "to the Power", e, "=",po)
    
power()
    
