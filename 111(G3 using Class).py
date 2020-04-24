class G_3():
       def __init__(self):
              self.a = int(input('Enter A : '))
              self.b = int(input('Enter B : '))
              self.c = int(input('Enter C : '))

       def process(self):
              if self.a == self.b and self.a == self.c:
                     print('All Numbers are Equal')
              elif self.a > self.b and self.a > self.c:
                     print(self.a,'is Greater than', self.b, '&', self.c)
              elif self.b > self.c:
                     print(self.b,'is Greater than', self.a, '&', self.c)
              else:
                     print(self.c,'is Greater than', self.a, '&', self.b)
obj = G_3()
obj.process()

                     
