s = "Python"
print(len(s))  # 6

 #without using len
s = "Python"

count = 0

for char in s:
    count += 1

print(count) #6

s = "Python"

count = 0
i = 0

while True:
    try:
        s[i]
        count += 1
        i += 1
    except IndexError:
        break

print(count)  #6

#adding 2numbers 
a=1
b=2
c=a+b
print(c)

#adding 2numbers withput using third variable
a=1
a = 1
b = 2

print(a + b)

a = 1
b = 2

print(sum([a, b]))

first = "Hello"
second = "World"

print(first + " " + second)

first = "Hello"
second = "World"

first += " " + second

print(first)