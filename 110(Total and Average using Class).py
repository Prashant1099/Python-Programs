class Total():
       def __init__(self, a, b, c):
               self.a = a
               self.b = b
               self.c = c

       def process(self):
              self.tot = self.a + self.b + self.c
              self.avg = self.tot/3
              
       def display(self):
              print('-------------------')
              print('Total   : ',self.tot)
              print('Average : ',self.avg)
              print('-------------------')

a = int(input("Enter First Number  : "))
b = int(input("Enter Second Number : "))
c = int(input("Enter Third Number  : "))

obj = Total(a, b, c)
obj.process()
obj.display()
       
       
      

       
