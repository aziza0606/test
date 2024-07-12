import os
os.system("cls") 

lst=[1,2,3,4,5]

lst[0],lst[1]=lst[1],lst[0]
lst[2],lst[3]=lst[3],lst[2]
print(lst)