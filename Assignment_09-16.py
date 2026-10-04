fruit1 = "apple"
fruit2 = "banana"
print(fruit1 == fruit2)   # False
print(fruit1 < fruit2)    # True (lexicographical)

COMPARISON WITHOUT ==

fruit1 = "apple"
fruit2 = "banana"

print(not (fruit1 != fruit2))

fruit1 = "apple"
fruit2 = "banana"

print(fruit1 is fruit2)

fruit1 = "apple"
fruit2 = "banana"

same = True

if len(fruit1) != len(fruit2):
    same = False
else:
    for i in range(len(fruit1)):
        if fruit1[i] != fruit2[i]:
            same = False
            break

print(same)


#isspace
name = "India "
print(name.isspace()) #false

name = "   "

print(name.isspace()) #True #only whitespace characters