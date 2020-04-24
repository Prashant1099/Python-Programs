from array import*

a1 = array('i', [])
r1 = int(input('Enter First Range  : '))


print("\nEnter",r1,"Elements")
print("------------------")

for i in range (r1):
       print("Enter Element",(i+1),":",end = ' ')
       e = int(input())
       a1.append(e)

#=============================================================

a2 = array('i', [])
r2 = int(input('\nEnter Second Range  : '))


print("\nEnter",r2,"Elements")
print("------------------")

for i in range (r2):
       print("Enter Element",(i+1),":",end = ' ')
       e = int(input())
       a2.append(e)

#=============================================================
c = array('i',[])
for i in range (r1):
       c.append(a1[i])

for i in range (r2):
       c.append(a2[i])

print("\nAfter Merging :")
print('----------------')
for i in range (r1 + r2):
       print(c[i])
