import os
os.system("cls") 

tup=(1,2,3,4)

lst=list(tup)

for i in range(len(lst)):
    lst[i]*=lst[i]
    print(lst[i])