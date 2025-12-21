# Finding length of a sttring
str1 = "chan"
length = len(str1)
print(length)

# String as an array
array1 = "apple"
array2 = "mango"

"""
A string is essentially a sequence of characters also called an array.
Thus we can access the elements of this array.

' variableName[start:stop:step] '
"""
print(array1[:3]) # app
print(array1[4]) # e
print(array2[::1]) # mango
print(array2[::2]) # mno
print(array1[::-1]) # elppa
print(array2[-1:-6]) # Empty #Python tries to move left to right, but -1 → -5 is right to left, which is impossible with a positive step.
print(array2[-1:-6:-1])
