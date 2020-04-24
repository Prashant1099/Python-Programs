r = int(input("Enter Range or Length of Array : "))
a = []

print("\nEnter",r,"Elements")
print("-----------------")

for i in range (r):
       print("Enter Element",(i+1),":",end = ' ')
       e = int(input())
       a.append(e)
     
tot = 0

for i in range (r):
       tot = tot + a[i]
avg = tot / r

print("\nTotal   = ",tot)
print("Average = ",avg)
