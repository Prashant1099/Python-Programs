def G_3():
    a = int(input("Enter A = "))
    b = int(input("Enter B = "))
    c = int(input("Enter C = "))

    if a == b and a == c:
           print('\nAll Numbers are Equal')
    elif a > b and a > c:
           print('\nA is Greater than All')
    elif b > c:
           print('\nB is Greater than All')
    else:
           print('\nC is Greater than All')

G_3()
           
