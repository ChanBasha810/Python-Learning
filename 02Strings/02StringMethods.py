# String method in python

# upper()
str1 = "chan"
print(str1.upper())

# lower()
str1 = "ChAn"
print(str1.lower())

# strip()
str1 = "     chan    "
print(str1)
print(str1.strip()) # removes the white spaces

# rstrip() - removes right side white spaces only
# lstrip() - removes left side white spaces only

# split()
str1 = "Chan Basha"
print(str1.split())

# capitalize()
str1 = "string methods in python"
print(str1.capitalize())

#title()
print(str1.title())

# replace()
str1 = "Hi, Chan!"
print(str1.replace("Hi", "Hello"))

#center()
print(str1.center(150))

# swapcase()
str1 = "Hello, chan BASHA"
print(str1.swapcase())

# startswith()
str1 = "chan basha"
print(str1.startswith("cha"))

# endswith()
print(str1.endswith("a"))

# find()
str1 = "chan"
print(str1.find("a"))
print(str1.find("b"))

# index()
print(str1.index("c"))
try:
    print(str1.index("z"))
except ValueError:
    print('''Traceback (most recent call last):
  File "/Users/chan/Fullstack 6_months/Python/02Strings/02StringMethods.py", line 56, in <module>
    print(str1.index("z"))
ValueError: substring not found''')

# isupper()
str1 = "CHAN"
print(str1.isupper())

# islower()
str2 = "chan"
print(str2.islower())

# istitle
str1 = "Chan Basha Is Back"
print(str1.istitle())

# isalnum() - checks only 0-1, a-z, A-Z
str1 = "Chan6"
print(str1.isalnum())

# isalpha() - checks only a-z, A-Z
str1 = "ChanBasha"
print(str1.isalpha())

# isprintable()
str1 = "chan"
str2 = "chan\n"
print(str1.isprintable()) # True
print(str2.isprintable()) # False