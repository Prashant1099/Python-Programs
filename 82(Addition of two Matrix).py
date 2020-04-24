rr = int(input("Enter Row Range of MATRIX A    : "))
cr = int(input("Enter Column Range of MATRIX A : "))
a_1 = []
sn = 1

# Initialization of Matrix

for row in range (rr):
       a_1.append([0] * cr)
print("\nEnter", rr,'x', cr, "Elememts of MATRIX A :")
       
#Input MATRIX

for row in range (rr):
       for col in range (cr):
              print("Enter", sn, "Number : ")
              a_1[row][col] = int(input())
              sn = sn + 1

#Display of MATRIX

print("\nMATRIX A Elemets are : ")
for row in range (rr):
       for col in range (cr):
              print(' ',a_1[row][col], end = ' ')
       print(' ')


#=========================================================================
rr = int(input("\nEnter Row Range of MATRIX B    : "))
cr = int(input("Enter Column Range of MATRIX B : "))
a_2 = []
sn = 1

# Initialization of Matrix

for row in range (rr):
       a_2.append([0] * cr)
print("\nEnter", rr,'x', cr, "Elememts of MATRIX B :")
       
#Input MATRIX

for row in range (rr):
       for col in range (cr):
              print("Enter", sn, "Number : ")
              a_2[row][col] = int(input())
              sn = sn + 1

#Display of MATRIX

print("\nMATRIX B Elemets are : ")
for row in range (rr):
       for col in range (cr):
              print(' ',a_2[row][col], end = ' ')
       print(' ')

#==============================================================================
a_3 = []
for row in range (rr):
       a_3.append([0] * cr)

print('\nAddition of MATRIX A & MATRIX B')
for row in range (rr):
       for col in range (cr):
              a_3[row][col] = a_1[row][col] + a_2[row][col]
              print(' ',a_3[row][col],end = ' ')
       print(' ')



