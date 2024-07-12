import os
os.system("cls") 

lst = [1, 2, 3, 4]
result = []


for i in range(len(lst) - 1):
    sum_elements = lst[i] + lst[i + 1]
    result.append(sum_elements)

print(lst)
print(result)
