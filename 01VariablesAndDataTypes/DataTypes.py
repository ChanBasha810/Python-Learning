# Python provides five types of built-in data types

# Number data types: int, float, complex
int1 = 18
float1 = 12.31
complex1 = 1+2j

print("Number data types: int, float, complex:-")
print(int1)
print(type(int1))
print(float1)
print(type(float1))
print(complex1)
print(type(complex1))
print("\n")

# Text data types: str
string1 = "hello!"
string2 = 'c'

print("Text data types: str:-")
print(string1)
print(type(string1))
print(string2)
print(type(string2))
print("\n")

# Boolean data types: True, False
bool1 = True
bool2 = False

print("Boolean data types: True, False:-")
print(bool1)
print(type(bool1))
print(bool2)
print(type(bool2))
print("\n")

# Sequence data types: list, tuple
list1 = [6, 2.1, "chan", [-4, 5], ['hi',"hello"]]
"""
A list is an ordered collection of data with elements seperated by a comma and enclosed within square bracketd.
Lists are mutable and can be modified after creation.
"""

print("Sequence data types: list, tuple:-")
print(list1)
print(type(list1))
print("\n")

tuple1 = ((1,2),("chan",'c'),(True, False), None, 36)
"""
A tuple same as list but enclosed within parantheses.
Tuples are immutable and can not be modified after creation.
"""
print(tuple1)
print(type(tuple1))
print("\n")

# Mapped data types: dict
dict1 = {"name":"chan", "age":15, "student":True, "EmailId":None}

"""
A dictionary is an unordered collection of data containing a key:value pair.
The key:value pairs are enclosed within curly brackets.
"""
print("Mapped data types: dict:-")
print(dict1)
print(type(dict1))