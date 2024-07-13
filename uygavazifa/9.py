from os import system
system("cls")

def func(dct):
    new=dict()
    for(key,value) in dct.items():
        print("key=",key,"\tvalue=",value)
        new[value]=key
    return new

natija=func({
    'salom':123,
    True:3.14,
    12:(40,"dunyo",3.14)
})

print(natija)