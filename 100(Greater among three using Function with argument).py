# With Argument 

def G_3(a, b, c):
       po = 1

       if a == b and a == c:
              print('\nAll Numbers are Equal')
       elif a > b and a > c:
              print('\nA is Greater than All')
       elif b > c:
              print('\nB is Greater than All')
       else:
              print('\nC is Greater than All')   

a = int(input("Enter A = "))
b = int(input("Enter B = "))
c = int(input("Enter C = "))
G_3(a, b, c)


    
    
