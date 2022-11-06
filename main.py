class Humen:
  def __init__(self, name):
    self.name = 'None'
    self.age = 0
    self.zarplata = 0

  def zarplatata2(self):
    self.zarplata += 0
    print(self.name  , 'заробатывает',  self.zarplata , 'грн')

  def zarplatata(self):
    self.zarplata += 20
    print(self.name  , 'заробатывает',  self.zarplata , 'грн')
    
  

    
class  Ychitel(Humen):
  def __init__(self):
    self.nastroienie = 'Хорошое настроение'
    self.name = 'Тамара Петровна'
    #self.age += 99
    self.zarplata = 2000
    
  
  def nastroienie1(self):
    print('У', self.name , self.nastroienie )
  
  

    
class Ychenik(Humen):
  def __init__(self):
    self.odeda = 'Модноя'
    self.name = 'Тарас'
    #self.age += 13
    self.zarplata = 20

  
  




obj2 = Ychenik()
obj2.zarplatata()

obj = Ychitel()
obj.zarplatata2()
obj.nastroienie1()