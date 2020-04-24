# A program which takes 5 Digit Number as input and Prints Reverse and Sum of those Digits

n = int(input("Enter any 5 Digit Number = "))
temp = n
length = 0

while (n > 0):
    n = n//10
    length += 1
print("\nLength of the Entered Number = ",length)

n = temp
while(length == 5):

    n1 = n % 10
    n  = n//10 
    n2 = n % 10
    n  = n//10
    n3 = n % 10
    n  = n//10
    n4 = n % 10
    n  = n//10
    n5 = n % 10

    tot = n1 + n2 + n3 + n4 + n5

    print("----------------------------------------")
    print("Reverse of {0}   = {1}{2}{3}{4}{5}".format(temp,n1,n2,n3,n4,n5))
    print("Summation of {0} = {1}".format(temp, tot))
    print("----------------------------------------")

else:
    print("Please Enter 5 Digit Number!!")
    n = int(input("\nEnter any 5 Digit Number = "))