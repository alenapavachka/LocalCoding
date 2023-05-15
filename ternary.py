#1

temperature = float(input('What\'s your body temperature: '))
print ('healthy') if temperature < 37 else print ('sick')

#2

num_of_day = int(input('Enter wich day of the it is 1-7: '))
print('work day') if num_of_day<=5 else print('weekend')

#3
number = int(input('Enter any number: '))
print (number * 2) if number > 0 else  print(- number)

#4

n = int(input('Enter your number:'))
print('Lucky number!') if  n%9 == 0 else print('Not a lucky number(')