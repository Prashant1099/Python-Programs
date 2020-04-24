rr = int(input("Enter Row Range : "))
cr = int(input("Enter Column Range : "))
a = []
sn = 1

# Initialization of Matrix
for row in range (rr):
       a.append([0] * cr)
print("\nEnter", rr,'x', cr, "Elememts of MATRIX :")
       

#Input MATRIX
for row in range (rr):
       for col in range (cr):
              print("Enter", sn, "Number : ",end=" ")
              a[row][col] = int(input())
              sn = sn + 1


#Display of MATRIX
print("\nMATRIX Elemets are : ")
for row in range (rr):
       for col in range (cr):
              print(' ',a[row][col], end = ' ')
       print(' ')
