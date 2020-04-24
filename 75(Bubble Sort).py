from array import*

a = array('i', [])
r = int(input("Enter Range or Length of Array : "))


print("\nEnter",r,"Elements")
print("----------------------")

for i in range (r):
       print("Enter Element",(i+1),":",end = ' ')
       e = int(input())
       a.append(e)

for i in range (r):
       for j in range (r-1):
              if a[j] > a[j+1]:
                     temp = a[j]
                     a[j] = a[j+1]
                     a[j+1] = temp

print("\nAfter Sort")
print("-------------")
for i in range (r):
       print(a[i])
              
