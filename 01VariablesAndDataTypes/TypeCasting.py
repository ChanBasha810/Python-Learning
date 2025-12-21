# TypeCasting in python

"""
There are two types of typecastings available in python
1.Implicit TypeCasting - int to float
2.Explicit TypeCasting - float to int
"""
# Implicit TypeCasting
a = 2
b = 3.1

sum1 = a+b
print(sum1)
print(type(a))
print(type(b))
print(type(sum1))
print("\n")

# Explicit TypeCasting
a = 10.002
b = 22

sum1 = a+b
print(sum1)
print(type(sum1))

sum2 = print(int(sum1))
print(type(sum2))