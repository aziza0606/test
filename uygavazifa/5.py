from os import system
system("cls")

def func(lst):
    kam={}
    for i in lst:
        if i in kam:
            kam[i]+=1
        else:
            kam[i]=1

    eng_kam=min(kam,key=kam.get)
    eng_kam=kam[eng_kam]

    return eng_kam

lst=[1,5,8,3,5,9,5,9,3,5,2,5,3,6,5,5,5]

natija=func(lst)
print(natija)
