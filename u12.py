import os
os.system("cls") 

tup=(10,20,30,40,50)

lst=list(tup)

ort=0

for i in range(len(lst)):
    ort+=lst[i]

ort=ort/5

print(ort)

