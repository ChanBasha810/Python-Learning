# Lists in python
marks = [3, 4, 18, "chan", True]
print(marks)
print(type(marks)) # <class 'list'>
print(marks[0]) # 3
print(marks[3]) # chan
print(marks[-1]) # True
print(marks[len(marks)-3]) # 18
print(marks[5-2]) # chan
print(marks[1:-1]) # [4, 18, 'chan']

lst = [i*i for i in range(10)]
print(lst) # [0 ,1 ,4 ,9, 16, 25, 36, 49, 64, 81]
lst2 = [i*i for i in range(10) if i%2==0] # Even
print(lst2) # [0, 4, 16, 36, 64]
lst2 = [i*i for i in range(10) if i%2!=0] # Odd
print(lst2) # [1, 9, 25, 49, 81]
