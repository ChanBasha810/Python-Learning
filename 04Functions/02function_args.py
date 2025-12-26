# Function arguments

# Default arg
def sum(a, b, c=1): # c=1 is default argument and optional
    print(a+b+c)
sum(2, 1)

# Keyword arg
def mul(a=2, b=3):
    print(a*b)
mul(b=4, a=5)

# Required arg
def sub(a, b):
    print(a-b)
sub(10, 4) # Two arguments required

# Variable-Length arg - *args, **kwargs

# *args
def total(*args):
    print(f"total = {args}")
    print(f"Length of total: {len(args)}")
    # print(sum(args))
total(1,2,3,4,5,6,7,8,8,67,67,67,6,7,65,6,5,45)

# **kwargs
def details(**kwargs):
    print(kwargs)
details(name="chan", age=5, status="student")