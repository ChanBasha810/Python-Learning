"""
if (condition):
    statements
elif (condition):
    statements
elif (condition):
    statements
    .
    .
    .
elif (condition):
    statements
else:
    statements
"""

value = int(input("Enter your age: "))

if 0 <= value <= 12:
    print("You are a child")
elif 13 <= value <= 19:
    print("You are younger")
elif 20 <= value <= 59:
    print("You are an adult")
elif value >= 60:
    print("You are older")
else:
    print("Invalid age")