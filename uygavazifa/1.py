from os import system
system("cls")

def func(lst):
    element=sorted(list(set(lst)))[-2]
    return element

lst=[1,2,3,4,5,6,7,8,9,9,10]
ikkinchiMax=func(lst)

print(ikkinchiMax)