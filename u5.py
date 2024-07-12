import os
os.system("cls")  

lst = [1, 2, 3, 4, 5, 6, 7, 8]


mid_index = len(lst) // 2
first_half = lst[:mid_index]
second_half = lst[mid_index:]


print(first_half)
print(second_half)