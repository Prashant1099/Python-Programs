class sum():
       def __init__(self):
              self.a = []
              self.r = int(input('Enter Range : '))
              self.tot = 0
                                 
       def input(self):
              print()
              for i in range(self.r):
                     print('Enter',i+1,'Number : ', end = '')
                     e = int(input())
                     self.a.append(e)

       def process(self):
              for i in range(self.r):
                     self.tot = self.tot + self.a[i]

       def display(self):
              print('\nToatal  : ',self.tot)
              print('Average : ',self.tot/self.r)


obj = sum()
obj.input()
obj.process()
obj.display()                                 
                                 
                     
