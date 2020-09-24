import random


list1 = [1, 2, 3, "hello", 7.0, 52]


nums = [1, 2, 3, 4, 5, 6, 7, 8]


nums = []

for i in range(1, 51):

    nums.append(i)

print(nums)    


nums = [i for i in range(1, 51)]

print(nums)


square_nums = []

for x in range( 1, 26):

    if x % 2 == 0:

        square_nums.append(x**2)

print(square_nums)


square_nums = [x**2 for x in range(1, 26) if x % 2 == 0]

print(square_nums)


Grades = {
    
    "Steven": 57,
    "Jessica": 82,
    "William": 42,
    "Hussein": 78,
    "Mary": 65   
}

print(Grades)


# Initialising empty dict
even_squared_dict = {}

for x in range( 1, 10):

    if x % 2 == 0:

        even_squared_dict[x] = x**2

print(even_squared_dict)


even_squared_dict = {x: x**2 for x in range(1, 10) if x % 2 == 0}

print(even_squared_dict)


ThreeCharCodes = ["CAN", "FIN", "FRA", "GAB", "HKG", "IMN"
                  "MCO", "NPL"]

cntryDict = {c: c[:2] for c in ThreeCharCodes}

print(cntryDict)


Fruits1 = set(["apple", "banana", "cherry", "peach"])
print(Fruits1)

Fruits2 = {"orange", "pear", "grape", "pear"}
print(Fruits2)


nums = set([])

for x in range(25):

    y = random.randint(10, 20)
    nums.add(y)

print(nums)


nums = {random.randint(10, 20) for num in range(25)}

print(nums)


kms = [10, 12, 65, 40, 12, 75, 34, 65, 10, 10, 38, 100, 160, 200]

miles = {d/1.6 for d in kms if d < 100}

print(miles)




