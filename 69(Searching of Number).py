r = int(input("Enter Range or Length of Array : "))
a = []

print("\nEnter",r,"Elements")
print("-----------------")

for i in range (r):
       print("Enter Element",(i+1),":",end = ' ')
       e = int(input())
       a.append(e)

po = 0

s = int(input("\nEnter Number you want to search : "))

for i in range (r):
       if s == a[i]:
              po = i + 1
              break       

if (po == 0):
       print(' ')
       print(s, "is not Found")
else:
       print(' ')
       print(s, "Found in Position", po)
