from os import system
system("cls")

def func(lst):
    kop={}
    for i in lst:
        if i in kop:
            kop[i]+=1
        else:
            kop[i]=1

    eng_kop=max(kop,key=kop.get)
    eng_kop1=kop[eng_kop]

    return eng_kop

lst=[1,5,8,3,5,9,5,9,3,5,2,5,3,6,5,5,5]

natija=func(lst)
print(natija)