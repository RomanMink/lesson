class Nasikomoe:
  def __init__ (self):
    self.spped = 30
    self.color = 'зелёный'
    self.vid = 'Таракан'

  def speed (self):
    print('скорость ', self.spped,'м в секунду' )

  def Maxspeed (self):
    self.spped += 300
    print('Когда', self.vid,'видет тапок скорость', self.spped,'м в секунду')

  
obj2 = Nasikomoe()
obj2.speed()
obj2.Maxspeed()