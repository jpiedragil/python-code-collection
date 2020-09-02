'''

Code from the article "Python Ten frequently used String Method with example"
Link: https://medium.com/@akash97715/python-ten-frequently-used-string-methods-7a7fded6e5e4

'''
# 1. Count

print(" 1. count() ".center(20, "*"))
print()

s = "The people of India works for the development of the country India"

print(s.count("India"))

print(s.count("India", 20, 80))

print()

# 2. center()

print(" 1. center() ".center(20, "*"))
print()

t = "akash"

print(t.center(16,"*"))

# 3. find()

print(" 3. find() ".center(20, "*"))
print()

print(s.find("India"))

# 4. swapcase()

print(" 4. swapcase() ".center(20, "*"))
print()

print(s.swapcase())

# 5. startswith() and endswith()

print(" 5. startswit() & endswith() ".center(20, "*"))
print()

print(s.startswith('The'))
print(s.startswith("people", 4, 30))

print()

print(s.endswith("India"))

# 6. split()

print(" 6. split() ".center(20, "*"))
print()

print(s.split(maxsplit=2))
print(s.split())

print()

# 7. capitalize(), upper(), string.title()

print(" 7. capitalize(), upper(), title() ".center(20, "*"))
print()

print(s.title())
print(s.upper())
print(s.capitalize())

print()

# 8. ljust(), rjust()

print(" 8. ljust() & rjust() ".center(20, "*"))
print()

s = "The"

print(s.ljust(40), "India is a great country")
print(s.rjust(40), "India is a great country")

print()

# 9. strip()

print(" 9. strip() ".center(20, "*"))
print()

s = "!!!!!!!!!!#!The people of India works for the development of the # country India!!!!!!!!!!"

print(s.strip("!#"))
print(s.lstrip("!#"))
print(s.rstrip("!#"))

print()

# 10. zfill()

print(" 10. zfill() ".center(20, "*"))
print()

s = "akash"

print(s.zfill(10))
print(s.zfill(5))
print(s.zfill(6))

print()
