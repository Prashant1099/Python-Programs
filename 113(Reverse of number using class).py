class Reverse():
       def __init__(self):
              self.n = int(input('Enter any Number : '))
              self.rev = 0
              self.n1 = self.n
              
       def process(self):
              while self.n > 0 :
                     self.mod = self.n % 10
                     self.rev = self.rev * 10 + self.mod
                     self.n = self.n // 10
                     
       def display(self):
              print('\nReverse of', self.n1, ':',self.rev)

obj = Reverse()
obj.process()
obj.display()
