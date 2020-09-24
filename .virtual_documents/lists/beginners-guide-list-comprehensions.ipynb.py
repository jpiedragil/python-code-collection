nums = [n for n in range(1, 6)]

print(nums)


nums = [1, 2, 3, 4, 5]

squares = [n * n for n in nums]

print(squares)


nums = [1, 2, 3, 4, 5]

odd_squares = [n * n for n in nums if n % 2 == 1]

print(odd_squares)


matrix = [[x for x in range(1, 4)] for y in range(1, 4)]

print(matrix)


matrix = [
    [x for x in range(1, 4)]
    for y in range(1, 4)
]

print(matrix)


people = [{
    "first_name": "Mata",
    "last_name": "Rosendall",
    "birthday": "9/25/1984"
}, {
    "first_name": "Sandra",
    "last_name": "O'Gaven",
    "birthday": "8/21/1995"
}]

birthdays = [
    person[term]
    for person in people
    for term in person
    if term == "birthday"
]

print(birthdays)



