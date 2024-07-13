from os import system
system("cls")

def func(dct):
    if not dct:
        print("bosh")
    else:
        max_key=max(dct.keys())
        print(max_key)

dct = {'a': 10, 'b': 20, 'c': 30}
func(dct)