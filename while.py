# Print all the even numbers from 1 to 30
x = 2
while x <= 30:
    print(x)
    x += 2

# Print floats from 0.2 to 3.4 with 0.2 step
x = 0.2
while x <= 3.4:
    print(round(x, 1))
    x += 0.2

# Find the sum of all the odd numbers from 5 to 41
s = 0
x = 5
while x <= 41:
    s = s + x
    x += 2
print(f'Sum = {s}')

# Multiply all from -1 to -11
mult = 1
x = -1
while x >= -11:
    mult = mult * x
    x -= 1
print(mult)

# Print a string that consists of 30 "z"
char = 'z'
n = 1
while n <= 30:
    print(char * n, len(char * n))
    n += 1

# Counting sheep
string = ""
x = 1
while x <= 20:
    string = string + str(x) + " sheep..."
    x += 1
print(string)

# Countdown
num = 10
st = ""
while num >= 1:
    st = st + str(num) + " seconds..."
    num -= 1
st = st[:-4]
print(st)

# Student learning progress
days = 1
words = 5
progress = 2
while days <= 22:
    words = words + progress
    days += 1
    progress += 2
print(words)

