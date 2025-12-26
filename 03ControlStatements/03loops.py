# Printing 1 to 100 numbers using for and while loops.

# For loop
for i in range(1, 101):
    print(i)
print("For loop - Done.")

# While loop
num = 1
while (num <= 100):
    print(num)
    num = num + 1
print("Wile loop - Done.")


# Do-while loop

"""
i = int(input("Enter the value: "))
print(i)
while i<=99:
    i = int(input("Enter the value: "))
    print(i)
"""

i = 1
while True:
    print(i)
    i = i + 1
    if i >= 101:
        break