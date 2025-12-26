"""
match variable_name:
    case 0:
        statements
    case 1:
        statements
    .
    .
    .

    case _ if(condition):
        statements
    case _:                  # Default case like else statement
        statements
    
"""

x = int(input("Enter your value: "))
y = 10
match x:
    case 0:
        print("0th case")
    case 1:
        print("1st case")
    case 2:
        print("2nd case")
    case 3:
        print("3rd case")
    case _:
        print(f"{x}th case") # use f-strings, str concatenation, or sep="" to control spacing.