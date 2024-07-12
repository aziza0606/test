import os
os.system("cls") 

tup = (-1,2,-3,4,-5)


lst = list(tup)

for i in range(len(lst)):
    if lst[i]>0:
        print(lst[i])
