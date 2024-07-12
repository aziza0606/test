import os
os.system("cls") 

lst=[1,2,3,4,5,6,7,8,9,10]
juft=[]
toq=[]

for i in range(len(lst)):
    if lst[i]%2==0:
        juft.append(lst[i])
    if lst[i]%2!=0:
        toq.append(lst[i])

print(juft)
print(toq)