from os import system
system("cls")

def func(dct,key):
    if key in dct:
        del dct[key]
    else:
        print(f"'{key}'nomli kalit mavjud emas.")

dct = {'a': 10, 'b': 20, 'c': 30}
func(dct,'b')
print(dct)

func(dct,'d')