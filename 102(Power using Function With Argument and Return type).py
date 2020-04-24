# With Argument and Return type

def power(b, e):
       po = 1

       for i in range (e):
           po = po  * b

       return po    

b = int(input("Enter Base = "))
e = int(input("Enter Expo = "))

ans = power(b, e)

print(b, "to the Power", e, "=",ans)
    
    
