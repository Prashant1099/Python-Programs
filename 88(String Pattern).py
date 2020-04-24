str = input("Enter String : " )
len = len(str)

print(' ')
print('Input String : ',str)

for row in range (len+1):
       for col in range (len-row):
              print(str[col], end = ' ')
       print(' ')
