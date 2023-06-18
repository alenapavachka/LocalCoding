# 1

char = input("Enter a character here: ")  
vowels = "a,e,i,o,u, y"
if char in vowels:
    print('vowel')
else:
    print("not a vowel")


# 2

name = input("Enter the name here: ")
vowels2 = "a,e,i,o,u,"
if name[0] not in vowels2:
    print("The name starts with a consanant")
else:
    print("Name starts with a vowel") 


# 3

string = input("Enter your text here: ")
range = "1,2,3,4,5,6,7,8,9"
if string[-1] in range: 
    print('true')
else:
    print('false')  

# 4

username = input('Enter your name: ')
if len(username) > 5:
    print('Your name is long!')
else:
    print("Your name is short!")         


# 5

answer  = input('Are you ok? ')

if answer =='No' or answer=='no':
    print('Get better!')
else:
    print('Cool!')    

# 6

a = int(input('Enter your first number: '))
b = int(input('Enter your second number: '))
if a % b == 0:
    print('yes')   
else:
    print('no')


# 7

user_name = input("Enter your name: ")
time = int(input('Enter the time in digits from 0-24: '))
if 0 <= time <= 6:
    print('Good night, ', user_name)
elif 7 <= time <= 11:
    print('Good morning, ', user_name)
elif 12 <= time <= 18:
    print('Good day, ', user_name)
elif 19 <= time <= 24:
     print('Good evening, ', user_name)
else:
    print('Wrong time')    


#8

price = float(input('Enter the price of the product: '))
if 300<=price:
    print('30% discount')
elif 200<=price:
    print('20% discount')    
elif 100<=price:
    print('10% discount')
else:
    print('no discount at this time')

#9

age= int(input('What\'s your age: '))
if age<16:
    print('children')
elif age<50:
    print('young man')   
else:
    print('senior')     

#10

current_color = ('red', 'yellow', 'green')
person = input('Enter "driver" or "pedestrian": ')
if person == 'driver':
    print(current_color)
else:
    print(current_color[::-1])
