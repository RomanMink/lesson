class Humen:
  def __init__(self, name):
    self.name = 'None'
    self.age = 0
    self.zarplata = 0

  def zarplatata2(self):
    self.zarplata += 0
    print(self.name+'а'  ,self.name2+'а', 'заробатывает',  self.zarplata , 'грн')

  def zarplatata(self):
    self.zarplata += 0
    print(self.name  , 'заробатывает',  self.zarplata , 'грн')
    
  

    
class  Ychitel(Humen):
  def __init__(self):
    self.nastroienie = 'Хорошое настроение'
    self.name = 'Тамар'
    self.name2 = 'Петровн'
    #self.age += 99
    self.zarplata = 2000
    
  
  def nastroienie1(self):
    print('У', self.name+'ы' ,self.name2+'ы', self.nastroienie )

  def zarplatatata(self):
    self.zarplata += 2000
    print(self.name+'е' , self.name2+'е','повышают зарплату до', self.zarplata ,'грн')
    
    
  
  

    
class Ychenik(Humen):
  def __init__(self):
    self.odeda = 'модно'
    self.name = 'Тарас'
    self.age = 0
    self.zarplata = 20
  
  def odeda1(self):
    print(self.name ,'одет',  self.odeda)
    
  def agee(self):
    self.age += 13
    print(self.name+'у',  self.age ,'лет')
  




obj2 = Ychenik()
obj2.zarplatata()
obj2.odeda1()
obj2.agee()

obj = Ychitel()
obj.zarplatata2()
obj.nastroienie1()
obj.zarplatatata()