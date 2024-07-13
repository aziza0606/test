from os import system
system("cls")

def func(lst):
    element=sorted(list(lst))
    return element

lst=[1,1,3,3,4,5,3,2,3,45,6,8,6,4,2,4,5,56]

sort_lst=func(lst)

print(sort_lst)