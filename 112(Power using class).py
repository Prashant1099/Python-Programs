class Pow():
       def __init__(self):
               self.b = int(input('Enter Base : '))
               self.e = int(input('Enter Expo : '))
               self.po = 1
               
       def process(self):
              for i in range (self.e):
                     self.po = self.po * self.b
                     
       def display(self):
              print(' ')
              print(self.b,"to the power",self.e," = ",self.po)

       
obj = Pow()
obj.process()
obj.display()
       
       
      

       
