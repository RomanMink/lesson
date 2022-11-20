class Transport:
  
  def __init__ (self):
    self.spped = 0
    self.name = 'none'
    self.sppeddoMax = 1
    

  def speed (self):
    print('')
    
class Car(Transport):


  def speed2 (self):
    print('Скорость Машины при розгоне:')
    print(self.spped)
    print(self.spped+5)
    print(self.spped+15)
    print(self.spped+50)
    print(self.spped+130)
    print(self.spped+190)
    print(self.spped+230)
    print(self.spped+240,'max')

  def s (self):
    print('Розгон до 100 на','Lambordgeni' )
    print('1секунда cкорост:',self.spped)
    print('1.5секунда cкорост:',self.spped+30)
    print('2секунда cкорост:',self.spped+50)
    print('3секунда cкорост:',self.spped+100)

    
class Velosiped(Transport):
  def __init__ (self):
    self.peredachi = 0
    self.sppeddoMax = 0
    self.spped = 0
    
  def t (self):
    print('передачи',self.peredachi+1,'и',7,'разгон до макс скорости за',self.sppeddoMax+7,'максимальная скорость ', self.spped+10)
    
    print('передачи',self.peredachi+2,'и',7,'разгон до макс скорости за',self.sppeddoMax+10,'максимальная скорость ', self.spped+17)
    
    print('передачи',self.peredachi+3,'и',7,'разгон до макс скорости за',self.sppeddoMax+25,'максимальная скорость ', self.spped+25)



  
  
obj2 = Transport()
obj2.speed()
obj = Car()
obj.speed2()
obj.s()
obj3 = Velosiped()
obj3.t()