# find sum from 1 to 100
s = 0
for i in range(1, 101):
    s += i
print(f'Sum = {s}')

# sum of all the odd numbers from 1 to 51
summa = 0
for i in range(1, 52):
    if i % 2 == 1:
        summa += i
print(summa)

# sum of all the even numbers in range 200-300
s1 = 0
for x in range(200, 301):
    if x % 2 == 0:
        s1 += x
print(s1)

# the number of integers
count = 0
for x in range(0, 1001):
    if x % 3 == 0:
        count += 1
print(count)

# sum and number
count1 = 0
s2 = 0
for x in range(0, 101):
    if x % 2 == 1:
        count1 += 1
    else:
        s2 += x
print(count1, s2)

# input the range
n = int(input("Find  the sum of even numbers in range from: "))
k = int(input("to: "))
s3 = 0
for x in range(n, k + 1):
    if x % 2 == 0:
        s3 += x
print(s3)



