# break
s = 0
while True:
    number = int(input("Enter a number: "))
    if number == 0:
        break
    s = s + number
print(s)

# continue
s1 = 0
for i in range(1, 101):
    if "7" in str(i):
        continue
    s1 += i
print(s1)

t = ''
s3 = "hello world"
for letter in s3:
    if letter == "o":
        continue
    t = t + letter + letter
print(t)

s5 = "May 9 is a weekend"
for letter in s5:
    if letter.isdigit():
        print("Yes")
        break
else:
    print("No")
