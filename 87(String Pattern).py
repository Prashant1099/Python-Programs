str = input("Enter String : " )
len = len(str)

print(' ')
print('Input String : ',str)

for row in range (len+1):
       for sp in range (len-row+2):
              print(end='  ')
       for col in range (row):
              print(str[col], end = ' ')
       print(' ')
