str = input("Enter String : " )
len = len(str)


for row in range (len+1):
       for col in range (row):
              print(str[col], end = ' ')
       print(' ')
