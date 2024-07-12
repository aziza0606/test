import os
os.system("cls")  

tup = (5, 3, 8, 1, 2)


lst = list(tup)

sum=0

for i in range(len(lst)):
    sum+=lst[i]

print(sum)