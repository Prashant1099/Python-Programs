str = input("Enter String : " )
len = len(str)

print('\nReverse of',str,': ', end = '')

for i in range (len-1, -1, -1):
       print(str[i], end = '')
