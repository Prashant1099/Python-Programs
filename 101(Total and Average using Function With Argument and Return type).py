# With Argument and Return type

def total(a,b,c):
    tot = a + b + c

    return tot    

a = int(input("Enter A = "))
b = int(input("Enter B = "))
c = int(input("Enter C = "))
ans = total(a,b,c)

print("\nTotal   = ",ans)
print("Average = ",round(ans/3,3))
    
