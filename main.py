#def reper(func):
#	def wrapper():
#		func()
#		print('он репер')
#	return wrapper

#def prichoska(func):
#	def wrapper():
#		func()
#		print('он лысый')
#	return wrapper
#
#def mauka(deco):
#	def wrapper():
#		deco()
#		print('он носит зелёную майку ')
#	return wrapper
#
#def shtani(deco):
#	def wrapper():
#		deco()
#		print('на нём штаны от  "Гуси" ')
#	return wrapper

#def zvet(deco):
#	def wrapper():
#		deco()
#		print('он чорный ')
#	return wrapper

#def vozrast(deco):
	#def wrapper():
	#	deco()
	#	print('ему 40 годиков ')
	#return wrapper


#@vozrast
#@zvet
#@shtani
#prichoska
#@mauka
#@reper
#def Chelovek():
#	print('Это человек')


#Chelovek()


















def ask_age():
  num1 = sign = num2 =''
  sign = ''
  num2 = ''
  while num1 == '' or sign == '' or num2 == '':
    try:
      num1 = int(input('Input your number 1: '))	
      num2 = int(input('Input your number 2: '))
      sign = input('Input your sign:')
      if sign == '+' or sign == '-' or sign == '*' or sign == '/':
        print(num1,sign,num2)
      else:
        sign = ''
        raise ValueError
    except ValueError:
      print('You need to write normal evaluation')

    if sing == '-':
        print(num1,sign,num2,'=',num1/num2)
    if sing == '*':
        print(num1,sign,num2,'=',num1*num2)
    if sign == '+':
      print(num1,sign,num2,'=',num1+num2)
    elif sign == '/':
      try:
        print(num1,sign,num2,'=',num1/num2)
      except:
        print('This is division by zero!!!')
    print('The end of program')
    
    
      
ask_age()