r = int(input("Enter Range or Length of Array : "))
a = []

print("\nEnter",r,"Elements")
print("-----------------")

for i in range (r):
       print("Enter Element",(i+1),":",end = ' ')
       e = int(input())
       a.append(e)

count = 0

s = int(input("\nEnter Number you want to search : "))

for i in range (r):
       if s == a[i]:
              count = count + 1

if (count == 0):
       print(s, "is not Found")
else:
       print(' ')
       print(s, "Found", count, "times")
