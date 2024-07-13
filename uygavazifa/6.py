from os import system
system("cls")

def func(dct):
    if not dct:
        print("bosh")
    else:
       max_value=max(dct.values())
       print(f"maximal:{max_value}")

dct = {'a': 10, 'b': 20, 'c': 30}
func(dct)