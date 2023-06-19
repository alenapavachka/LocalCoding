# 1
st = input("Enter a phrase/ word here:  ")
for x in range(len(st)):
    print(x, st[x])

# 2
s = input("Enter a word here:  ")
for i in range(len(s)):
    print(s[i], " - ", i)

# 3
s1 = "Chef Executive Officer"
count = 0
for letter in s1:
    if letter.isupper():
        count += 1
print(count)

# 4
vowels = "aeiouAEIOU"
count1 = 0
s3 = input("Enter your word here: ")
for char in s3:
    if char in vowels:
        count1 += 1
print(count1)

# 5
st4 = "summer"
res = ""
for i, letter in enumerate(st4):
    if i % 2 == 0:
        res = res + letter.upper()
    else:
        res = res + letter.lower()
print(res)


