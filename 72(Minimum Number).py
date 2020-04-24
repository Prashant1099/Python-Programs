r = int(input("Enter Range or Length of Array : "))
a = []

print("\nEnter",r,"Elements")
print("-----------------")

for i in range (r):
       print("Enter Element",(i+1),":",end = ' ')
       e = int(input())
       a.append(e)

min = a[0]

for i in range (r):
       if min >= a[i]:
              min = a[i]

print("\nMinimum Number : ",min)
