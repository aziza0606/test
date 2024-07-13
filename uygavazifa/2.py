from os import system
system("cls")

def min2(lst):
    element=sorted(list(set(lst)))[1]
    return element

lst=[1,2,3,4,5,6,7,8,9,10]

ikkinchiMin=min2(lst)

print(ikkinchiMin)