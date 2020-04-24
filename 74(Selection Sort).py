r = int(input("Enter Range or Length of Array : "))
a = []

print("\nEnter",r,"Elements")
print("-----------------")

for i in range (r):
       print("Enter Element",(i+1),":",end = ' ')
       e = int(input())
       a.append(e)

for i in range (r-1):
       for j in range (i+1, r):
              if a[i] > a[j]:
                     temp = a[i]
                     a[i] = a[j]
                     a[j] = temp

print("\nAfter Sorting")
print('--------------')

for i in range (r):
       print(a[i])
