r = int(input("Enter Range or Length of Array : "))
a = []

print("\nEnter",r,"Elements")
print("----------------")

for i in range (r):
       print("Enter Element",(i+1),":",end = ' ')
       e = int(input())
       a.append(e)

max = a[0]

for i in range (r):
       if max <= a[i]:
              max = a[i]

print("\nMaximum Number : ",max)
